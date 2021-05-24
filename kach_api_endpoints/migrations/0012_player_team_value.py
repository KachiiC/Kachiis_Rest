# Generated by Django 3.1.4 on 2021-05-24 19:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach_api_endpoints', '0011_player_points_on_transfers'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team_value',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2000)]),
            preserve_default=False,
        ),
    ]
