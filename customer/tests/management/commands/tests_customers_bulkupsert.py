from django.test import TestCase
from django.core.management import call_command
from django.db.models import Q

from customer.management.commands.customers_bulkupsert import Command
from io import StringIO
from customer.models import Customer

import json
import os
import responses
from dotenv import load_dotenv

load_dotenv()

here = os.path.abspath(os.path.dirname(__file__))


class TestsCustomersBulkUpsert(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            first_name='test',
            last_name='test last name',
            email='luke@darkside.com',
            gender='Male',
            company='stars',
            city='Osasco, SP',
            title='Jedi',
            latitude='-23.533385',
            longitude='-46.7914568'
        )

    def active_responses(self):
        token = os.getenv('TOKEN')
        path = {'path': os.path.join(here, '../../infrastructure/google_maps/customers.csv')}
        customers = Command.customers(kwargs=path)
        id_locations = self.id_location(customers)
        n = 0
        json_file = open(
            os.path.join(
                here,
                '../../infrastructure/google_maps/google_response/response.json'))
        response = json.load(json_file)

        for location in id_locations:
            responses.add(responses.GET,
                          f'https://maps.googleapis.com/maps/api/geocode/json?key={token}&address={location["city"]}',
                          json=response[n], status=200)
            n += 1
        return responses

    @staticmethod
    def id_location(customer):
        id_locations = []
        for c in customer:
            id_locations.append(
                {"id": c['id'],
                 "city": c['city']}
            )
        return id_locations

    def test_create_customer(self):
        self.assertIsNotNone(self.customer)

    @responses.activate
    def test_customers_bulkupsert_success(self):
        self.active_responses()
        out = StringIO()

        call_command('customers_bulkupsert',
                     path=os.path.join(here,
                                       '../../infrastructure/google_maps/customers.csv'), stdout=out)
        customers = Customer.objects.filter(~Q(latitude=''))

        assert len(customers) == 3
