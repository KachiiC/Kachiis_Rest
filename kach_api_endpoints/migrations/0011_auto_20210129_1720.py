# Generated by Django 3.1.4 on 2021-01-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach_api_endpoints', '0010_auto_20210129_1716'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chips',
            new_name='Chip',
        ),
        migrations.RemoveField(
            model_name='player',
            name='chips',
        ),
        migrations.AddField(
            model_name='player',
            name='chip',
            field=models.ManyToManyField(blank=True, to='kach_api_endpoints.Chip'),
        ),
    ]
