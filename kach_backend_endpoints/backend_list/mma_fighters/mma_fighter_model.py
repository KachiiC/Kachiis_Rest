from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

status_choices = (
    ('Active', 'active'),
    ('Retired', 'retired')
)

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

validator_condition = validators = [
    MinValueValidator(50),
    MaxValueValidator(100)
]


class Fighter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=status_choices)
    date_of_birth = models.DateField()
    height = models.CharField(max_length=10)
    reach = models.DecimalField(max_digits=3, decimal_places=1)
    weight_class = models.CharField(max_length=15, choices=weight_class_choices)
    promotion = models.CharField(max_length=50)
    rank = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    wins = models.IntegerField(validator_condition)
    losses = models.IntegerField(validator_condition)
    draws = models.IntegerField(validator_condition, default=0)
    no_contests = models.IntegerField(validator_condition, default=0)
    wins_via_knockout = models.IntegerField(validator_condition)
    wins_via_submission = models.IntegerField(validator_condition)
    wins_via_decision = models.IntegerField(validator_condition)
    losses_via_knockout = models.IntegerField(validator_condition)
    losses_via_submission = models.IntegerField(validator_condition)
    losses_via_decision = models.IntegerField(validator_condition)
    notable_wins = models.ManyToManyField('Fight', blank=True)
    highlights = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
