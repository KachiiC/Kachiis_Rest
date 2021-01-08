from rest_framework import serializers
# My Models
from .mma_dictionary_model import Dictionary


class DictionarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Dictionary
        fields = ['title', 'type', 'example_type', 'example', 'definition']
