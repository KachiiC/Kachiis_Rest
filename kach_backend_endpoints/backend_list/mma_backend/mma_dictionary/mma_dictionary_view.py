from rest_framework.response import Response
from rest_framework.decorators import api_view
from .mma_dictionary_model import Dictionary
from .mma_dictionary_serializer import DictionarySerializer


@api_view(['GET'])
def mma_dictionary_list(request):
    data = Dictionary.objects.all()

    serializer = DictionarySerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)
