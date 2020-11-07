from rest_framework import serializers
from .imdb_model import Content, ImdbList


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ("title", "imdb_id", "content_type", "media_type", "release_date")


class ImdbListSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = ImdbList
        fields = ("content_type", "list_title", "content", "media_type")

