from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=100)
    imdb_id = models.CharField(max_length=20)
    content_type = models.CharField(max_length=20)
    media_type = models.CharField(max_length=20)
    released = models.IntegerField()


class ImdbList(models.Model):
    list_title = models.CharField(max_length=20)
    content_type = models.CharField(max_length=20)
    media_type = models.CharField(max_length=20, default="movie")
    content = models.ManyToManyField("Content", blank=True)
