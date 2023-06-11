from .models import *
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        depth = 2


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        depth = 2

class MenuItem(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
        depth = 2


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
        depth = 2
