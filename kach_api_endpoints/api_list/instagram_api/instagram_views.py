from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from .instagram_serializers import InstaPostSerializer
import requests
import json
import os
from kach_api_endpoints.api_list.instagram_api.instagram_model import Post
from kach_api_endpoints.management.repoppers.instagram_repoppers import create_insta_data

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/instagram/instagramData.json"


@method_decorator(cache_page(60 * 60 * 2))
@api_view(['GET'])
def instagram_posts_list(request):

    url = "https://instagram-data1.p.rapidapi.com/user/feed"

    querystring = {
        "username": "basically_mma"
    }

    headers = {
        'x-rapidapi-key': "985371e109mshb5666c0424d5dcfp1b7485jsndf2afe5a3591",
        'x-rapidapi-host': "instagram-data1.p.rapidapi.com"
    }

    insta_response = requests.request(
        "GET", url, headers=headers, params=querystring
    ).json()

    with open(OUTFILE_LOCATION, 'w', encoding='utf8') as json_file:
        json_file.write(
            json.dumps(insta_response, indent=4, ensure_ascii=False)
        )

    Post.objects.all().delete()

    create_insta_data(OUTFILE_LOCATION)

    data = Post.objects.all()

    serializer = InstaPostSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)
