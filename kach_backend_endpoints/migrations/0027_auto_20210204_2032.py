# Generated by Django 3.1.4 on 2021-02-04 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kach_backend_endpoints', '0026_auto_20210204_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fighter',
            old_name='isChampion',
            new_name='is_champion',
        ),
    ]