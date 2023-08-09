import requests
from django.conf import settings

TOMTOM_API_KEY = settings.TOMTOM_API_KEY
# https://developer.tomtom.com/routing-api/documentation/routing/calculate-route


class TomTomGateway(object):
    url = f'https://api.tomtom.com/routing/1/calculateRoute/'

    def __init__(self):
        pass

    def get_route(self, address1,  address2):
        # '52.50931,13.42936:52.50274,13.43872/json?\
        #     instructionsType=text&language=en-US\
        #     &vehicleHeading=90&sectionType=traffic\
        #     &report=effectiveSettings&routeType=eco\
        #     &traffic=true&avoid=unpavedRoads\
        #     &travelMode=car&vehicleMaxSpeed=120\
        #     &vehicleCommercial=false&vehicleEngineType=combustion\
        #     &key={TOMTOM_API_KEY}'

        lat1 = address1.latitude
        lat2 = address2.latitude
        long1 = address1.longitude
        long2 = address2.longitude

        preferences = {
            # 'instructionsType': 'text',
            # 'language': 'en-US',
            # 'avoid': 'unpavedRoads',
            # 'routeType': 'eco',
            # 'travelMode': 'car',
            # 'vehicleCommercial': 'false',
            'key': TOMTOM_API_KEY
        }

        resp = requests.get(self.url + f'{lat1},{long1}:{lat2},{long2}/json', params=preferences, headers={'accept': '*/*'})
        if int(resp.status_code) == 200:
            return resp.json()
        else:
            raise Exception("Error with TomTom: ", resp.content)
