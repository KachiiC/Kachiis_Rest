from django.db import models

type_choices = status_choices = (
    ('Image', 'GraphVideo'),
    ('Video', 'GraphImage')
)


class Post(models.Model):
    post_link = models.CharField(max_length=100)
    caption = models.TextField()
    media = models.TextField()
    type = models.CharField(choices=type_choices, max_length=50)
    time_stamp = models.BigIntegerField()
    thumbnail = models.TextField()
    likes = models.IntegerField()
    user = models.CharField(max_length=100)
    user_id = models.BigIntegerField()
