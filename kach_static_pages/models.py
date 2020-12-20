from django.db import models


class DisplayCard(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    card_link = models.CharField(max_length=50)
    image_url = models.CharField(max_length=50)
