# Generated by Django 3.1.1 on 2020-12-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach_backend_endpoints', '0002_word_hsk_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='definition',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
