from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .instagram_model import Post
from .instagram_serializers import InstaPostSerializer


@api_view(['GET'])
def instagram_posts_list(request):
    data = Post.objects.all()

    serializer = InstaPostSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)