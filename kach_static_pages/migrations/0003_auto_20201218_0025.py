# Generated by Django 3.1.4 on 2020-12-18 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach_static_pages', '0002_auto_20201217_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displaycard',
            name='card_image',
            field=models.ImageField(default='default.jpg', upload_to='card_images'),
        ),
    ]
