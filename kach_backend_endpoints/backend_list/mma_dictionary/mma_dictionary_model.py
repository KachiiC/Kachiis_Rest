from django.db import models


class Dictionary(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=50, null=True, blank=True)
    example = models.CharField(max_length=50, null=True, blank=True)
    example_type = models.CharField(max_length=50, null=True, blank=True)
    definition = models.TextField(max_length=2000)

    def __str__(self):
        return self.name
