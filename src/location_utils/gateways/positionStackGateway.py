import requests
from django.conf import settings

POSITION_STACK_API_KEY = settings.POSITION_STACK_API_KEY



class PositionStackGateway(object):
    url = 'http://api.positionstack.com/v1/'

    def search_by_text(self, query):
        payload = {'access_key': settings.POSITION_STACK_API_KEY, 'query': query}
        resp = requests.get('http://api.positionstack.com/v1/forward', params=payload)
        if resp.status_code != '200':
            raise Exception('PositionStack Error', resp.content)
