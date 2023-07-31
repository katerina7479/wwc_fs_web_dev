from django.test import TestCase
from unittest.mock import patch
import json
from src.location_utils.us_address import *



class AddressTextCase(TestCase):

    san_francisco_address = {
        'display_name': '855 Harrison St, San Francisco, CA 94107',
        'latitude': '37.780109',
        'longitude': '-122.400497'
    }

    new_york_address = {
        'display_name': '555 5th Ave New York NY 10017 US',
        'latitude': '40.755810',
        'longitude': '-73.978750'
    }

    near_sf = {
        'display_name': '72 Ellis St, San Francisco, CA 94102',
        'latitude': '37.785782',
        'longitude': '-122.407532'
    }

    near_ny = {
        'display_name': '149 East 39Th Street, New York City, NY',
        'latitude': '40.749141',
        'longitude': '-73.976295'
    }


    @staticmethod
    def _get_route_response():
        with open('src/tests/location_utils/route_response.json') as fp:
            return json.loads(fp.read())

    def test_address_parse(self):
        text_addr = '123 Main St. Suite 100 Chicago, IL'
        addr = USAddress(text_addr)

        self.assertEqual(addr.street_number, '123')
        self.assertEqual(addr.street_name, 'Main St.')
        self.assertEqual(addr.subaddress, 'Suite 100')
        self.assertEqual(addr.city, 'Chicago')
        self.assertEqual(addr.state, 'IL')

    def test_double_place(self):
        text_addr = '318 East 51st Street, Kansas City, MO 64112'
        addr = USAddress(text_addr)

        self.assertEqual(addr.street_number, '318')
        self.assertEqual(addr.street_name, 'East 51st Street')
        self.assertEqual(addr.city, 'Kansas City')
        self.assertEqual(addr.state, 'MO')
        self.assertEqual(addr.zipcode, '64112')

    @patch.object(GeoCodeMapsGateway, 'search_by_text', return_value=new_york_address)
    def test_geocoding(self, mock_gateway):
        text_addr = '555 5th Ave New York NY 10017 US'
        addr = USAddress(text_addr)
        addr.validate_address_and_geocode()
        self.assertTrue(mock_gateway.called)
        self.assertEqual(addr.latitude, float(self.new_york_address['latitude']))
        self.assertEqual(addr.longitude, float(self.new_york_address['longitude']))


    def test_sf_distance(self):
        addr1 = USAddress(latitude=self.san_francisco_address['latitude'], longitude=self.san_francisco_address['longitude'])
        addr2 = USAddress(latitude=self.near_sf['latitude'], longitude=self.near_sf['longitude'])

        distance = addr1.estimate_distance(addr2, 'mile')
        self.assertEqual(distance, 0.5489874448025793)

        addr1 = USAddress(latitude=self.new_york_address['latitude'], longitude=self.new_york_address['longitude'])
        addr2 = USAddress(latitude=self.near_ny['latitude'], longitude=self.near_ny['longitude'])

        distance = addr1.estimate_distance(addr2)
        self.assertEqual(distance, 0.770070676529982)

    def test_long_distance(self):
        addr1 = USAddress(latitude=self.san_francisco_address['latitude'],
                          longitude=self.san_francisco_address['longitude'])
        addr2 = USAddress(latitude=self.new_york_address['latitude'], longitude=self.new_york_address['longitude'])

        distance = addr1.estimate_distance(addr2, 'mile')
        # actual: 2,572
        self.assertEqual(distance, 2566.124199305059)

    @patch.object(TomTomGateway, 'get_route', return_value=_get_route_response())
    def test_route(self, mock_gateway):
        addr1 = USAddress(latitude=self.san_francisco_address['latitude'], longitude=self.san_francisco_address['longitude'])
        addr2 = USAddress(latitude=self.near_sf['latitude'], longitude=self.near_sf['longitude'])

        travel_miles, travel_minutes = addr1.driving_distance(addr2)
        self.assertTrue(mock_gateway.called)
        self.assertEqual(travel_miles, 1.681)
        self.assertEqual(travel_minutes, 9.516666666666667)
