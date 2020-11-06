from rest_framework import serializers
from kach_api_endpoints.api_list.youtube_api.youtube_model import YoutubeVideo, YoutubePlaylist


class YoutubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = ("video_title", "video_id", "video_description", "upload_date",
                  "video_thumbnail", "playlist_id", "channel_id")


class YoutubePlaylistSerializer(serializers.ModelSerializer):
    playlist_videos = YoutubeVideoSerializer(many=True, read_only=True)

    class Meta:
        model = YoutubePlaylist
        fields = ('playlist_name', "playlist_id", "playlist_videos")
