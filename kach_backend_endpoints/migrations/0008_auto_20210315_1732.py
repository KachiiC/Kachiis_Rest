# Generated by Django 3.1.4 on 2021-03-15 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach_backend_endpoints', '0007_auto_20210315_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
