import os
import json
import requests
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .instagram_serializers import InstaPostSerializer
from kach_api_endpoints.api_list.instagram_api.instagram_model import Post
from kach_api_endpoints.management.repoppers.instagram_repoppers import create_insta_data
from rest_framework import views

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/instagram/instagramData.json"


class InstagramPostApiView(views.APIView):

    @method_decorator(cache_page(60 * 60 * 24 * 7))
    def get(self, request):
        url = "https://instagram40.p.rapidapi.com/account-medias"

        querystring = {
            "userid": "32817560066",
            "first": "50",
            "after": "QVFDOGV6dGFtQnJXdnZ0a1FuMkFLSjRHYjdWMEdTTFltMkZpd1FvcUxuQXZ6bDJFVnpKRzFYU3RMSUoyNXluOXFZUVZ3dG1YM3NSTEJqMVI3TTBKM0ZTNg=="
        }

        headers = {
            'x-rapidapi-key': "985371e109mshb5666c0424d5dcfp1b7485jsndf2afe5a3591",
            'x-rapidapi-host': "instagram40.p.rapidapi.com"
        }

        insta_response = requests.request("GET", url, headers=headers, params=querystring).json()

        with open(OUTFILE_LOCATION, 'w', encoding='utf8') as json_file:
            json_file.write(
                json.dumps(insta_response, indent=4, ensure_ascii=False)
            )

        data = Post.objects.all()

        data.delete()
        create_insta_data(OUTFILE_LOCATION)

        serializer = InstaPostSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
