# Generated by Django 3.1.4 on 2021-01-12 15:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach_backend_endpoints', '0010_auto_20210108_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Active', 'active'), ('Retired', 'retired')], max_length=15)),
                ('date_of_birth', models.DateField()),
                ('promotion', models.CharField(max_length=50)),
                ('rank', models.CharField(max_length=100)),
                ('height', models.IntegerField(validators=[django.core.validators.MinValueValidator(4), django.core.validators.MaxValueValidator(8)])),
                ('reach', models.IntegerField(validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(100)])),
                ('weight_class', models.CharField(max_length=25)),
                ('wins', models.IntegerField(verbose_name=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(100)])),
                ('losses', models.IntegerField(verbose_name=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(100)])),
                ('draws', models.IntegerField(default=0, verbose_name=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(100)])),
                ('no_contests', models.IntegerField(default=0, verbose_name=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(100)])),
                ('style', models.CharField(max_length=100)),
                ('notable_wins', models.CharField(max_length=100)),
                ('wins_via_knockout', models.IntegerField(verbose_name=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(100)])),
                ('wins_via_submission', models.IntegerField(verbose_name=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(100)])),
                ('wins_via_decision', models.IntegerField(verbose_name=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(100)])),
                ('losses_via_knockout', models.IntegerField(verbose_name=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(100)])),
                ('losses_via_submission', models.IntegerField(verbose_name=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(100)])),
                ('losses_via_decision', models.IntegerField(verbose_name=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]