from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Song(models.Model):
    chart_number = models.IntegerField("Chart_Position", validators=[MinValueValidator(1), MaxValueValidator(100)])
    artist = models.CharField(max_length=200)
    song_title = models.CharField(max_length=300)
