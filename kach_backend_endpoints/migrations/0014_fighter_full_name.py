# Generated by Django 3.1.4 on 2021-06-16 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach_backend_endpoints', '0013_fighter_highlights'),
    ]

    operations = [
        migrations.AddField(
            model_name='fighter',
            name='full_name',
            field=models.CharField(default='full name', max_length=100),
            preserve_default=False,
        ),
    ]
