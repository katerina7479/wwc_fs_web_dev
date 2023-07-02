from .models import *
from rest_framework import serializers
from src.models.validators import validate_email_address, validate_password


class AdminUserSerialiser(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[validate_email_address])
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = AdminUser
        fields = ["first_name", "last_name", "email", "is_active", "password"]

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
        depth = 2


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
        depth = 2


class MenuItem(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"
        depth = 2


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"
        depth = 2
