# Generated by Django 3.1.4 on 2020-12-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('card_link', models.CharField(max_length=50)),
                ('card_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
