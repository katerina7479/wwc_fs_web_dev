import cuid
from django.db import models
from django.contrib.postgres.fields import ArrayField

from src.models.validators import validate_days_of_week, day_abbreviations


# Create your models here.
# Location model
class Location(models.Model):
    id = models.CharField(primary_key=True, default=cuid.cuid, max_length=25, editable=False)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')
    address = models.TextField()
    phone = models.CharField(max_length=30)
    deletedAt = models.DateTimeField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'location'


# Menu model
class Menu(models.Model):
    id = models.CharField(primary_key=True, default=cuid.cuid, max_length=25, editable=False)
    name = models.CharField(max_length=255)
    items = models.ManyToManyField('MenuItem', related_name='menus')
    deletedAt = models.DateTimeField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'menu'


# MenuItem model
class MenuItem(models.Model):
    id = models.CharField(primary_key=True, default=cuid.cuid, max_length=25, editable=False)
    section = models.ForeignKey('MenuSection', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    picture = models.ImageField(upload_to='menu_items/')
    deletedAt = models.DateTimeField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'menu_item'


# MenuSection model
class MenuSection(models.Model):
    id = models.CharField(primary_key=True, default=cuid.cuid, max_length=25, editable=False)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'menu_section'


# Schedule model
class Schedule(models.Model):
    id = models.CharField(primary_key=True, default=cuid.cuid, max_length=25, editable=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    days_of_week = ArrayField(
        models.CharField(max_length=3, choices=[(d, d) for d in day_abbreviations]),
        validators=[validate_days_of_week], null=True, blank=True
    )
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    precedence = models.IntegerField(default=5)
    deletedAt = models.DateTimeField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'schedule'

    def save(self, *args, **kwargs):
        self.days_of_week = sorted(
            self.days_of_week,
            key=lambda day: day_abbreviations.index(day))
        super().save(*args, **kwargs)
