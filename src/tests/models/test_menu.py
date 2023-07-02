from django.core.files.base import ContentFile
from django.test import TestCase
from faker import Faker
from src.models import *


fake = Faker()


class LocationTestCase(TestCase):
    def setUp(self):
        name = "Pseudo-Diner"
        logo = ContentFile(fake.image(), name=f"{name.lower().replace(' ', '_')}.png")
        address = fake.address()
        phone = fake.phone_number()

        location = Location(name=name, address=address, phone=phone)
        location.logo.save(logo.name, logo)
        location.save()

    def test_location_name(self):
        location = Location.objects.first()
        self.assertEqual(location.name, "Pseudo-Diner")
