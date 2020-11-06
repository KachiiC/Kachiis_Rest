from django.db import models


class YoutubeVideo(models.Model):
    video_title = models.CharField(max_length=500)
    video_id = models.CharField(max_length=50)
    video_description = models.TextField()
    upload_date = models.DateTimeField()
    video_thumbnail = models.CharField(max_length=300)
    playlist_id = models.CharField(max_length=50)
    channel_id = models.CharField(max_length=50)


class YoutubePlaylist(models.Model):
    playlist_name = models.CharField(max_length=200)
    playlist_id = models.TextField(max_length=35)
    playlist_videos = models.ManyToManyField('YoutubeVideo', blank=True)
