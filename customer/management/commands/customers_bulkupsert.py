import csv
import os
from django.core.management import BaseCommand

from customer.infrastructure.google_maps.google_maps_client import GoogleMapsClient
from customer.models import Customer

here = os.path.abspath(os.path.dirname(__file__))


class Command(BaseCommand):
    help = 'Load customers csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    @staticmethod
    def customers(kwargs):
        path = kwargs['path']
        with open(path, 'rt') as customers:
            lines = csv.reader(customers, delimiter=',')
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

    def handle(self, *args, **kwargs):
        customers = self.customers(kwargs)
        id_locations = self.id_location(customers)
        locations = self.get_locations_(id_locations)
        for customer in customers:
            get_position = self.get_data_location_by_id(locations, customer)
            create_customer = Customer.objects.create(
                first_name=customer['first_name'],
                last_name=customer['last_name'],
                email=customer['email'],
                gender=customer['gender'],
                company=customer['company'],
                city=customer['city'],
                title=customer['title'],
                latitude=get_position.latitude,
                longitude=get_position.longitude
            )

    @staticmethod
    def id_location(customer):
        id_locations = []
        for c in customer:
            id_locations.append(
                {"id": c['id'],
                 "city": c['city']}
            )
        return id_locations

    @staticmethod
    def get_locations_(locations):
        return GoogleMapsClient().get_geo_location(locations)

    @staticmethod
    def get_data_location_by_id(locations, customer):
        for location in locations:
            if location.id == customer['id']:
                return location

