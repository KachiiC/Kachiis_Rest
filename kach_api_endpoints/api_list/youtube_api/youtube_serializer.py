from rest_framework import serializers
from kach_api_endpoints.api_list.youtube_api.youtube_model import YoutubeVideo, YoutubePlaylist


class YoutubeVideoSerializer(serializers.ModelSerializer):

    upload_date = serializers.DateTimeField("%d/%m/%Y")

    class Meta:
        model = YoutubeVideo
        fields = [
            "video_title",
            "video_id",
            "video_description",
            "video_thumbnail",
            "upload_date",
        ]


class YoutubePlaylistSerializer(serializers.ModelSerializer):
    playlist_videos = YoutubeVideoSerializer(many=True, read_only=True)

    class Meta:
        model = YoutubePlaylist
        fields = [
            'playlist_name',
            "playlist_id",
            "playlist_videos"
        ]
