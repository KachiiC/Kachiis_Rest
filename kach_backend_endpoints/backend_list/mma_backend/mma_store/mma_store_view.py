from rest_framework.response import Response
from rest_framework.decorators import api_view
from .mma_store_model import StoreItem
from .mma_store_serializer import StoreSerializer


@api_view(['GET'])
def mma_store_list(request):
    data = StoreItem.objects.all()

    serializer = StoreSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)
