from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

validator_condition = validators = [
    MinValueValidator(0),
    MaxValueValidator(100)
]


class Fighter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    weight_class = models.CharField(max_length=100)
    fighter_image = models.CharField(max_length=500)
    height = models.CharField(max_length=10)
    rank = models.IntegerField(null=True, blank=True)
    p4p_ranking = models.IntegerField(null=True, blank=True)
    is_champion = models.BooleanField(default=False)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(60)])
    reach = models.DecimalField(max_digits=4, decimal_places=1)
    wins = models.IntegerField()
    losses = models.IntegerField()
    draws = models.IntegerField(default=0)
    wins_via_ko = models.IntegerField()
    wins_via_sub = models.IntegerField()
    wins_via_dec = models.IntegerField()
    status = models.CharField(max_length=100)
    legend = models.BooleanField(default=False)
    highlights = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
