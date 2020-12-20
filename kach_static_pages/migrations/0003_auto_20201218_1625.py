# Generated by Django 3.1.4 on 2020-12-18 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach_static_pages', '0002_auto_20201218_0224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='displaycard',
            name='card_image',
        ),
        migrations.AddField(
            model_name='displaycard',
            name='image_url',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
    ]
