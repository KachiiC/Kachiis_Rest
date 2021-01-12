from django.db import models
from kach_backend_endpoints.backend_list.mma_fighters.mma_fighter_model import Fighter

winner_choices = (
    ('Red Corner', 'red'),
    ('Blue Corner', 'blue'),
    ('None', 'none')
)

method_of_victory_choices = (
    ('Knockout', 'ko'),
    ('Technical Knockout', 'tko'),
    ('Submission', 'sub'),
)

draw_choices = (
    ('Yes', 'yes'),
    ('No', 'no')
)


class Fight(models.Model):
    red_corner = models.OneToOneField(
        Fighter,
        related_name="red_corner",
        blank=True,
        on_delete=models.CASCADE
    )
    blue_corner = models.OneToOneField(
        Fighter,
        related_name="blue_corner",
        blank=True,
        on_delete=models.CASCADE
    )
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
    draw = models.CharField(
        max_length=10,
        choices=draw_choices,
        default='no'
    )
    title = models.CharField(max_length=100)
    video = models.CharField(max_length=25)
    event = models.CharField(max_length=100)
    date = models.DateField()
