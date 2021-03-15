from rest_framework import serializers
from kach_backend_endpoints.backend_list.mma_backend.mma_articles.mma_articles_model import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "title",
            "thumbnail_url",
            "post_time_stamp",
            "post_description"
        ]
