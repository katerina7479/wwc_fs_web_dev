# Generated by Django 4.2.2 on 2023-06-11 02:11

import cuid
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.CharField(default=cuid.cuid, editable=False, max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='logos/')),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('deletedAt', models.DateTimeField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.CharField(default=cuid.cuid, editable=False, max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('deletedAt', models.DateTimeField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='MenuSection',
            fields=[
                ('id', models.CharField(default=cuid.cuid, editable=False, max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'menu_section',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.CharField(default=cuid.cuid, editable=False, max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('days_of_week', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, null=True, size=None)),
                ('date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('precedence', models.IntegerField(default=5)),
                ('deletedAt', models.DateTimeField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.location')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.menu')),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.CharField(default=cuid.cuid, editable=False, max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('picture', models.ImageField(upload_to='menu_items/')),
                ('deletedAt', models.DateTimeField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.menusection')),
            ],
            options={
                'db_table': 'menu_item',
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='items',
            field=models.ManyToManyField(related_name='menus', to='src.menuitem'),
        ),
    ]
