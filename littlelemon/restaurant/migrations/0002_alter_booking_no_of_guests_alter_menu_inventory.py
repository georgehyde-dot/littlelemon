# Generated by Django 4.1.5 on 2023-01-23 19:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
