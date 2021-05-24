from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class MatchDay(models.Model):
    player_id = models.IntegerField(blank=True, default=12345)
    gameweek = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(38)])
    game_week_points = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)])
    points_total = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5000)])
    team_value = models.IntegerField(validators=[MinValueValidator(500), MaxValueValidator(2000)])
    game_week_transfers = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(15)])
    game_week_transfers_cost = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)])
    bench_points = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])


class Player(models.Model):
    player_name = models.CharField(max_length=150)
    team_name = models.CharField(max_length=1000)
    player_id = models.IntegerField()
    points_total = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    points_on_transfers = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
    transfers_total = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(570)])
    team_value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2000)])
    current_gameweek = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(38)])
    last_gameweek_points = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2000)])
    matches = models.ManyToManyField('MatchDay', blank=True)
    chips = models.ManyToManyField('Chip', blank=True)


class Chip(models.Model):
    chip_owner = models.CharField(max_length=150)
    chip_name = models.CharField(max_length=150)
    chip_date = models.DateTimeField()
    chip_matchday = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(38)])
