from rest_framework import viewsets
from src.models.serializers import *
from src.models.models import *


# Create your views here.
class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


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
