# Generated by Django 3.1.4 on 2020-12-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach_static_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displaycard',
            name='card_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
