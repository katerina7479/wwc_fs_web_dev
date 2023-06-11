import random

from django.core.exceptions import ValidationError
from faker import Faker
from django.core.files.base import ContentFile
from .sample_data import *
from ..models.models import *

fake = Faker()


def create_fake_location():
    name = fake.company()
    logo = ContentFile(fake.image(), name=f"{name.lower().replace(' ', '_')}.png")
    address = fake.address()
    phone = fake.phone_number()

    location = Location(name=name, address=address, phone=phone)
    location.logo.save(logo.name, logo)
    location.save()
    return location

def create_fake_menu():
    name = fake.bs()
    menu = Menu(name=name)
    menu.save()
    return menu


def create_fake_menu_section(menu):
    # Pick a random section name
    section_name = random.choice(list(sample_menu_items.keys()))
    # Check if the section already exists for the provided menu
    section, created = MenuSection.objects.get_or_create(name=section_name)

    for _ in range(random.randint(3, 7)):  # Adjust the number of menu items as needed
        item_name = random.choice(sample_menu_items[section_name])
        description = fake.sentence(nb_words=12)
        price = round(random.uniform(1, 50), 2)
        menu_item = MenuItem(name=item_name, description=description, price=price, section=section)
        menu_item.save()
        menu.items.add(menu_item)
        menu.save()

    return section


def create_fake_schedule(location, menu):
    # Generate a random name, days_of_week, date, start_time, end_time, and precedence
    name = fake.bs()
    days_of_week = random.sample(day_abbreviations, k=random.randint(1, 7))
    date = fake.date_between(start_date='-1y', end_date='today') if random.random() < 0.5 else None
    start_time = fake.time_object()
    end_time = fake.time_object()
    precedence = random.randint(1, 10)

    schedule = Schedule(
        location=location, menu=menu, name=name, days_of_week=days_of_week,
        date=date, start_time=start_time, end_time=end_time, precedence=precedence
    )
    try:
        schedule.full_clean()
        schedule.save()
        return schedule
    except ValidationError as e:
        print(f"ValidationError: {e}")
        return None


def create_fake_set():
    location = create_fake_location()
    menus = [create_fake_menu() for _ in range(2)]
    for menu in menus:
        create_fake_schedule(location, menu)
        create_fake_menu_section(menu)
