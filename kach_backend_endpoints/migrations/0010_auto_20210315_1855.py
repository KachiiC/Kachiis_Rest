# Generated by Django 3.1.4 on 2021-03-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach_backend_endpoints', '0009_auto_20210315_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeitem',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
