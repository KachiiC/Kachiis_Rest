# Generated by Django 3.1.4 on 2021-01-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach_api_endpoints', '0012_auto_20210129_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='chip',
            name='chip_owner',
            field=models.CharField(default='name', max_length=150),
            preserve_default=False,
        ),
    ]