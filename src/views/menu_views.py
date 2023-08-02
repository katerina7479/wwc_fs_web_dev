from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from src.models.serializers import *
from src.models.models import *


# Create your views here.
class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

    @action(detail=True, methods=['GET'])
    def distance(self, request, pk=None):
        params = request.query_params
        lat = params.get('lat')
        lon = params.get('lon')
        if not (lat or lon):
            Response("Requires latitude and longitude", status.HTTP_400_BAD_REQUEST)

        location_model = self.get_object()
        location_address = location_model.address_object()
        query_address = USAddress(latitude=lat, longitude=lon)
        response = location_address.estimate_distance(query_address, unit='mile')
        return Response({"miles": response})



class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Menu.objects.all()


class MenuSectionViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSectionSerializer
    queryset = MenuSection.objects.all()

class MenuItemViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = MenuItem.objects.all()


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
