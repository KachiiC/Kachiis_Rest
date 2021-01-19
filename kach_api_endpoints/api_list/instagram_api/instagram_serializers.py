from rest_framework import serializers
from .instagram_model import Post


class InstaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "media",
            "user",
            "user_id",
            "post_link",
            "caption",
            "type",
            "time_stamp",
            "thumbnail",
            "likes",
            "views"
        ]
