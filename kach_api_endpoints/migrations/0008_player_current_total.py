# Generated by Django 3.1.1 on 2020-12-07 15:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach_api_endpoints', '0007_imdblist_media_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='current_total',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
            preserve_default=False,
        ),
    ]
