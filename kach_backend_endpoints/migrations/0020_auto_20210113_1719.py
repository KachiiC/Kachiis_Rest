# Generated by Django 3.1.4 on 2021-01-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach_backend_endpoints', '0019_auto_20210113_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='fight',
            name='blue_pre_fight',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fight',
            name='red_pre_fight',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fighter',
            name='highlights',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
