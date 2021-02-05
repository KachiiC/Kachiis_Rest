# Generated by Django 3.1.4 on 2021-02-05 17:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('value', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=45)),
                ('suit', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('example', models.CharField(blank=True, max_length=50, null=True)),
                ('example_type', models.CharField(blank=True, max_length=50, null=True)),
                ('definition', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Fight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red_corner', models.CharField(max_length=50)),
                ('blue_corner', models.CharField(max_length=50)),
                ('red_pre_fight', models.CharField(max_length=15)),
                ('blue_pre_fight', models.CharField(max_length=15)),
                ('winner', models.CharField(blank=True, choices=[('Red Corner', 'red'), ('Blue Corner', 'blue'), ('None', 'none')], max_length=25)),
                ('method_of_victory', models.CharField(blank=True, choices=[('Knockout', 'ko'), ('Technical Knockout', 'tko'), ('Submission', 'sub'), ('Decision', 'dec')], max_length=25)),
                ('round', models.CharField(choices=[(1, 'first'), (2, 'second'), (3, 'third'), (4, 'forth'), (5, 'fifth')], max_length=20)),
                ('draw', models.BooleanField(default=False)),
                ('weight_class', models.CharField(choices=[(105, 'atom'), (115, 'straw'), (125, 'fly'), (135, 'bantam'), (145, 'feather'), (155, 'light'), (170, 'welter'), (185, 'middle'), (205, 'light_heavy'), (265, 'heavy')], max_length=25)),
                ('title_fight', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('video', models.CharField(blank=True, max_length=25, null=True)),
                ('event', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('notable_win', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('weight_class', models.CharField(max_length=100)),
                ('fighter_image', models.CharField(max_length=500)),
                ('height', models.CharField(max_length=10)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('is_champion', models.BooleanField(default=False)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(60)])),
                ('reach', models.DecimalField(decimal_places=1, max_digits=4)),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('draws', models.IntegerField(default=0)),
                ('wins_via_ko', models.IntegerField()),
                ('wins_via_sub', models.IntegerField()),
                ('wins_via_dec', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('discipline', models.CharField(max_length=100)),
                ('difficulty', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=3000)),
                ('tutorial', models.CharField(max_length=100)),
                ('mistakes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_characters', models.CharField(max_length=10)),
                ('pinyin', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=50)),
                ('definition', models.CharField(blank=True, max_length=100)),
                ('hsk_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
            ],
        ),
        migrations.CreateModel(
            name='HSKLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('words', models.ManyToManyField(blank=True, to='kach_backend_endpoints.Word')),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_class', models.CharField(choices=[('Fly', 'Flyweight'), ('Bantam', 'Bantamweight'), ('Feather', 'Featherweight'), ('Light', 'Lightweight'), ('Welter', 'Welterweight'), ('Middle', 'Middleweight'), ('Light Heavy', 'Light Heavyweight'), ('Heavy', 'Heavyweight')], max_length=15)),
                ('gender', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women')], default='Men', max_length=15)),
                ('pound_for_pound', models.BooleanField(default=False)),
                ('fighters', models.ManyToManyField(blank=True, to='kach_backend_endpoints.Fighter')),
            ],
        ),
    ]
