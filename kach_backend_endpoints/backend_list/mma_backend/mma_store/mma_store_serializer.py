from rest_framework import serializers
from .mma_store_model import StoreItem


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreItem
        fields = [
            "name",
            "price",
            "product_thumbnail",
            "product_link"
        ]
