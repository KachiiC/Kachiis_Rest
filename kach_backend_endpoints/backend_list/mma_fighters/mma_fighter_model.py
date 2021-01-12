from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

status_choices = (
    ('Active', 'active'),
    ('Retired', 'retired')
)

validator_condition = validators = [MinValueValidator(50), MaxValueValidator(100)]


class Fighter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=status_choices)
    date_of_birth = models.DateField()
    promotion = models.CharField(max_length=50)
    rank = models.CharField(max_length=100)
    height = models.CharField(max_length=10)
    reach = models.DecimalField(max_digits=3, decimal_places=1)
    weight_class = models.IntegerField(validators=[MinValueValidator(105), MaxValueValidator(265)])
    style = models.CharField(max_length=100)
    notable_wins = models.CharField(max_length=100)
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

    def __str__(self):
        return self.last_name
