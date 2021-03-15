from django.db import models


class StoreItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_thumbnail = models.CharField(max_length=500)
