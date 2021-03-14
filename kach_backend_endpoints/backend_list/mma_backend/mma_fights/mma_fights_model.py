from django.db import models

winner_choices = (
    ('Red Corner', 'red'),
    ('Blue Corner', 'blue'),
    ('None', 'none')
)

method_of_victory_choices = (
    ('Knockout', 'ko'),
    ('Technical Knockout', 'tko'),
    ('Submission', 'sub'),
    ('Decision', 'dec')
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

first = 1
second = 2
third = 3
fourth = 4
fifth = 5

round_choices = (
    (first, 'first'),
    (second, 'second'),
    (third, 'third'),
    (fourth, 'forth'),
    (fifth, 'fifth'),
)


class Fight(models.Model):
    red_corner = models.CharField(max_length=50)
    blue_corner = models.CharField(max_length=50)
    red_pre_fight = models.CharField(max_length=15)
    blue_pre_fight = models.CharField(max_length=15)
    winner = models.CharField(
        max_length=25,
        choices=winner_choices,
        blank=True
    )
    method_of_victory = models.CharField(
        max_length=25,
        choices=method_of_victory_choices,
        blank=True
    )
    round = models.CharField(max_length=20, choices=round_choices)
    draw = models.BooleanField(default=False)
    weight_class = models.CharField(max_length=25, choices=weight_class_choices)
    title_fight = models.BooleanField(default=False)
    description = models.TextField()
    video = models.CharField(max_length=25, blank=True, null=True)
    event = models.CharField(max_length=100)
    date = models.DateField()
    notable_win = models.BooleanField(default=True)
