from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class MatchDay(models.Model):
    player_id = models.IntegerField(blank=True, default=12345)
    game_week = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(38)])
    game_week_points = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)])
    points_total = models.IntegerField(default=100, validators=[MinValueValidator(1), MaxValueValidator(5000)])
    team_value = models.IntegerField(validators=[MinValueValidator(500), MaxValueValidator(2000)])
    game_week_transfers = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(15)])
    game_week_transfers_cost = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)])
    bench_points = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])


class Player(models.Model):
    player_name = models.CharField(max_length=150)
    player_id = models.IntegerField()
    matches = models.ManyToManyField('MatchDay', blank=True)
