from rest_framework.response import Response
from rest_framework.decorators import api_view
from .mma_techniques_model import Technique
from .mma_techniques_serializer import TechniquesSerializer


@api_view(['GET'])
def mma_techniques_list(request):
    data = Technique.objects.all()

    serializer = TechniquesSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)
