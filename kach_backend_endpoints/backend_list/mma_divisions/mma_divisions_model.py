from django.db import models

weight_class_choices = (

    ("Fly", "Flyweight"),
    ("Bantam", "Bantamweight"),
    ("Feather", "Featherweight"),
    ("Light", "Lightweight"),
    ("Welter", "Welterweight"),
    ("Middle", "Middleweight"),
    ("Light Heavy", "Light Heavyweight"),
    ("Heavy", "Heavyweight")
)

gender_choices = (
    ("Men", "Men"),
    ("Women", "Women")
)


class Division(models.Model):
    weight_class = models.CharField(max_length=35, choices=weight_class_choices)
    fighters = models.ManyToManyField('Fighter', blank=True)
    gender = models.CharField(max_length=15, choices=gender_choices, default="Men")
    pound_for_pound = models.BooleanField(default=False,)

    def __str__(self):
        return f"{self.weight_class}"
