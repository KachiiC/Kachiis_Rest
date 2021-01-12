from rest_framework.response import Response

from rest_framework.decorators import api_view
from .mma_fighter_model import Fighter
from .mma_fighter_serializer import FighterSerializer


@api_view(['GET'])
def mma_fighter_list(request):
    data = Fighter.objects.all()

    serializer = FighterSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)
