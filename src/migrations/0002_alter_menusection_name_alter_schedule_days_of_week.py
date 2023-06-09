# Generated by Django 4.2.2 on 2023-06-11 03:34

import django.contrib.postgres.fields
from django.db import migrations, models
import src.models.validators


class Migration(migrations.Migration):
    dependencies = [
        ("src", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menusection",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="days_of_week",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("Mon", "Mon"),
                        ("Tue", "Tue"),
                        ("Wed", "Wed"),
                        ("Thu", "Thu"),
                        ("Fri", "Fri"),
                        ("Sat", "Sat"),
                        ("Sun", "Sun"),
                    ],
                    max_length=3,
                ),
                blank=True,
                null=True,
                size=None,
                validators=[src.models.validators.validate_days_of_week],
            ),
        ),
    ]
