import requests


class GeoCodeMapsGateway(object):
    url = 'https://geocode.maps.co/search'


    def search_by_text(self, query):
        # [{'place_id': 10139899, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
        #   'powered_by': 'Map Maker: https://maps.co', 'osm_type': 'node', 'osm_id': 1000793154,
        #   'boundingbox': ['40.7557728', '40.7558728', '-73.9788465', '-73.9787465'], 'lat': '40.7558228',
        #   'lon': '-73.9787965',
        #   'display_name': 'Barnes & Noble, 555, 5th Avenue, Midtown East, Manhattan, New York County, New York, 10017, United States',
        #   'class': 'shop', 'type': 'books', 'importance': 0.621},
        #  {'place_id': 27213973, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
        #   'powered_by': 'Map Maker: https://maps.co', 'osm_type': 'node', 'osm_id': 2716012085,
        #   'boundingbox': ['40.7557517', '40.7558517', '-73.9787914', '-73.9786914'], 'lat': '40.7558017',
        #   'lon': '-73.9787414',
        #   'display_name': '555, 5th Avenue, Midtown East, Manhattan, New York County, New York, 10017, United States',
        #   'class': 'place', 'type': 'house', 'importance': 0.621}]

        resp = requests.get(self.url, params={'q': query})
        if resp.status_code != 200:
            raise Exception('GeocodeMapsError', resp.content)

        data = resp.json()
        if len(data) > 1:
            # sort by importance and take the highest
            data = sorted(data, key=lambda d: d['importance'])
        if len(data) == 0:
            return None
        place = data[0]
        return {
            'display_name': place['display_name'],
            'latitude': place['lat'],
            'longitude': place['lon']
        }
