# Generated by Django 5.0.6 on 2024-06-12 12:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_place_longitude', models.FloatField()),
                ('start_place_latitude', models.FloatField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('start_hour', models.TimeField()),
                ('end_hour', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('travel_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='api.itinerary')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveIntegerField()),
                ('itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='api.itinerary')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='api.place')),
            ],
            options={
                'ordering': ['itinerary', 'day'],
                'unique_together': {('itinerary', 'day', 'place')},
            },
        ),
    ]
