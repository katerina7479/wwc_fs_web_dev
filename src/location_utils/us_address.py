import usaddress
from .gateways import TomTomGateway, GeoCodeMapsGateway
import math


# The parse method will split your address string into components, and label each component.
# expected output: [(u'123', 'AddressNumber'), (u'Main', 'StreetName'), (u'St.', 'StreetNamePostType'), (u'Suite', 'OccupancyType'), (u'100', 'OccupancyIdentifier'), (u'Chicago,', 'PlaceName'), (u'IL', 'StateName')]



ADDRESS_MAPPING = {
    'PlaceName': 'city',
    'StateName': 'state',
    'ZipCode': 'zipcode',
}

for Label in usaddress.LABELS:
    if 'AddressNumber' in Label:
        ADDRESS_MAPPING[Label] = 'street_number'
    elif 'StreetName' in Label:
        ADDRESS_MAPPING[Label] = 'street_name'
    elif 'Subaddress' in Label or 'Occupancy' in Label:
        ADDRESS_MAPPING[Label] = 'subaddress'


class USAddress(object):
    geocode_gateway = GeoCodeMapsGateway()
    routes_gateway = TomTomGateway()

    def __init__(self, text_address=None, latitude=None, longitude=None):
        if not (text_address or (latitude and longitude)):
            raise Exception("US Address object requires either text_address or latitude longitude")

        self.text_address = text_address
        self.street_number = None
        self.street_name = None
        self.subaddress = None
        self.city = None
        self.state = None
        self.zipcode = None
        self.latitude = float(latitude) if latitude else None
        self.longitude = float(longitude) if longitude else None
        if text_address:
            self._normalize_address()

    def _normalize_address(self):
        parsed_address, address_type = usaddress.tag(self.text_address)

        attrs = {v: [] for _, v in ADDRESS_MAPPING.items()}
        attrs['other'] = []

        for label, value in parsed_address.items():
            if 'USPSBox' in label:
                raise Exception('Not supporting PO Boxes')

            target_attr = ADDRESS_MAPPING.get(label, 'other')
            attrs[target_attr].append(value)

        for attr_name, values in attrs.items():
            setattr(self, attr_name, ' '.join(values) or None)


    def validate_address_and_geocode(self):
        resp = self.geocode_gateway.search_by_text(self.text_address)
        if not resp:
            raise Exception("Address not found")
        self.latitude = float(resp['latitude'])
        self.longitude = float(resp['longitude'])


    def validate_geocode(self):
        if not (self.latitude and self.longitude):
            raise Exception("Both Latitude and longitude required")


    def estimate_distance(self, address, unit='km'):
        # =acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(lon2-lon1))*6371
        self.validate_geocode()
        address.validate_geocode()

        R_earth_km = 6372.8
        R_earth_miles = 3959.87433

        lat1 = math.radians(self.latitude)
        lat2 = math.radians(address.latitude)
        dLat = math.radians(self.latitude - address.latitude)
        dLon = math.radians(self.longitude - address.longitude)

        # math's trig functions require floats as inputs
        a = math.sin(dLat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dLon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))

        if unit == 'km':
            return R_earth_km * c
        elif unit == 'mile':
            return R_earth_miles * c


    def driving_distance(self, address, unit='km'):
        resp = self.routes_gateway.get_route(self, address)
        summary = resp["routes"][0]["summary"]
        length_meters = summary['lengthInMeters']
        travel_minutes = summary['travelTimeInSeconds'] / 60.0

        if unit == 'km':
            return length_meters / 1000.0, travel_minutes
        else:
            return length_meters * 0.000621371, travel_minutes




