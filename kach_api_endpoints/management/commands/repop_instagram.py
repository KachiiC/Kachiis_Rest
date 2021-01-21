import requests
from django.core.management.base import BaseCommand
import requests
import json
import os
from kach_api_endpoints.api_list.instagram_api.instagram_model import Post
from kach_api_endpoints.management.repoppers.instagram_repoppers import create_insta_data

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/instagram/instagramData.json"


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Pulling data from API...")

        url = "https://instagram-data1.p.rapidapi.com/user/feed"

        querystring = {"username": "basically_mma"}

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

        print("Data successfully pulled from API...")

        Post.objects.all().delete()

        print("Repopping Insta Data...")

        create_insta_data(OUTFILE_LOCATION)

        print("Successfully prepped Insta!")
