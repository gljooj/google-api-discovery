import csv
import json
import os
import pytest

from django.test import TestCase
import unittest
import requests
from django.core import management
from io import StringIO

import responses
from customer.infrastructure.google_maps.google_maps_client import GoogleMapsClient
from django.core.management import call_command

here = os.path.abspath(os.path.dirname(__file__))


# Create your tests here.
class Tests(TestCase):

    def test_command(self):
        args = [os.path.join(here, 'infrastructure/google/customers.csv')]
        out = StringIO()
        call_command("customers_bulkupsert",  *args, stdout=out, stderr=StringIO())
        self.assertEquals(out.getvalue(),
            "I don't feel like dancing Rock'n'Roll.")

    @pytest.yield_fixture
    def active_responses(self):
        json_file = open(
            os.path.join(
                here,
                'infrastructure/google/google_response/response.json'))

        response = json.load(json_file)
        responses.add(responses.GET, f'https://maps.googleapis.com/maps/api/geocode/json?', json=response, status=200)

        return responses

    @responses.activate
    def test_customers_bulkupsert(self):
        args = [os.path.join(here, 'infrastructure/google/customers.csv')]
        opts = {}
        a = call_command('customers_bulkupsert', *args, **opts)
        b = ''

    @staticmethod
    def customers():
        with open(os.path.join(here, '../../../customers.csv'), encoding='utf-8') as arquivo_referencia:
            lines = csv.reader(arquivo_referencia, delimiter=',')
            items = []
            for line in lines:
                if line[0] == 'id':
                    continue
                items.append(
                    {
                        "id": line[0],
                        "first_name": line[1],
                        "last_name": line[2],
                        "email": line[3],
                        "gender": line[4],
                        "company": line[5],
                        "city": line[6],
                        "title": line[7],
                    }
                )

        return items

    @staticmethod
    def id_location(customer):
        id_locations = []
        for c in customer:
            id_locations.append(
                {"id": c['id'],
                 "city": c['city']}
            )
        return id_locations

    def get_locations_(self, locations):
        return GoogleMapsClient().get_geo_location(locations)

    def get_data_location_by_id(self, locations, customer):
        for l in locations:
            if l.id == customer['id']:
                return l

    def test_api(self):
        customers = self.customers()
        id_locations = self.id_location(customers)
        # criar um for para separar um dict de id, city
        locations = self.get_locations_(id_locations)
        for c in customers:
            check_position = self.get_data_location_by_id(locations, c)

        key = 'AIzaSyDc7QuWmkb6PcJFuYKySnj6KbW3B0Y4Tfc'

        address = 'Warner, NH'

        params = {'key': key, 'address': [address]}

        base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        response = requests.get(base_url, params)
        a = response.json()
