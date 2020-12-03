from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Word(models.Model):
    chinese_characters = models.CharField(max_length=10)
    pinyin = models.CharField(max_length=30)
    type = models.CharField(max_length=50)
    definition = models.CharField(max_length=100, blank=True)
    hsk_level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])


class HSKLevel(models.Model):
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    words = models.ManyToManyField('Word', blank=True)
