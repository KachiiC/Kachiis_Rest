from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250)
    thumbnail_url = models.CharField(max_length=250)
    post_time_stamp = models.CharField(max_length=50)
    post_description = models.CharField(max_length=250)
    post_link = models.CharField(max_length=250)
