from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

Atom = 105
Straw = 115
Fly = 125
Bantam = 135
Feather = 145
Light = 155
Welter = 170
Middle = 185
Light_Heavy = 205
Heavy = 265

weight_class_choices = (
    (Atom, 'atom'),
    (Straw, 'straw'),
    (Fly, 'fly'),
    (Bantam, 'bantam'),
    (Feather, 'feather'),
    (Light, 'light'),
    (Welter, 'welter'),
    (Middle, 'middle'),
    (Light_Heavy, 'light_heavy'),
    (Heavy, 'heavy'),
)

rank_validator_condition = validators = [
    MinValueValidator(1),
    MaxValueValidator(15)
]

validator_condition = validators = [
    MinValueValidator(0),
    MaxValueValidator(100)
]


class Fighter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rank = models.IntegerField(rank_validator_condition, null=True, blank=True)
    is_champion = models.BooleanField(default=False)
    weight_class = models.CharField(max_length=15, choices=weight_class_choices)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(60)])
    height = models.CharField(max_length=10)
    reach = models.DecimalField(max_digits=4, decimal_places=1)
    wins = models.IntegerField(validator_condition)
    losses = models.IntegerField(validator_condition)
    draws = models.IntegerField(validator_condition, default=0)
    wins_via_ko = models.IntegerField(validator_condition)
    wins_via_sub = models.IntegerField(validator_condition)
    wins_via_dec = models.IntegerField(validator_condition)
    fighter_image = models.CharField(max_length=250)

    # highlights = models.CharField(max_length=100, blank=True)
    # notable_wins = models.ManyToManyField('Fight', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
