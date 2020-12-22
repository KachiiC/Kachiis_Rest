from django.db import models


class Card(models.Model):
    code = models.CharField(max_length=2)
    value = models.CharField(max_length=5)
    image = models.CharField(max_length=45)
    suit = models.CharField(max_length=8)
