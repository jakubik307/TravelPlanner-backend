# Generated by Django 5.0.6 on 2024-06-17 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_visit_geometry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='geometry',
        ),
    ]
