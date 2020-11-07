# Generated by Django 3.1.1 on 2020-11-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach_api_endpoints', '0004_auto_20201107_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('imdb_id', models.CharField(max_length=20)),
                ('content_type', models.CharField(max_length=20)),
                ('media_type', models.CharField(max_length=20)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ImdbList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_title', models.CharField(max_length=20)),
                ('content_type', models.CharField(max_length=20)),
                ('content', models.ManyToManyField(blank=True, to='kach_api_endpoints.Content')),
            ],
        ),
    ]
