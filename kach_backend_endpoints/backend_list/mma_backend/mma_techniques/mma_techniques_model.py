from django.db import models


class Technique(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    discipline = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    description = models.TextField(max_length=3000)
    tutorial = models.CharField(max_length=100)
    mistakes = models.CharField(max_length=100)

    def __str__(self):
        return self.title
