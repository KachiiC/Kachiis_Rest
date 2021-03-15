from django.db import models


class StoreItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_thumbnail = models.CharField(max_length=500)
    product_link = models.CharField(max_length=250)
