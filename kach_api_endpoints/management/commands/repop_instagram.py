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

        url = "https://easy-instagramapi.p.rapidapi.com/v1/profile/basically_mma/media"

        headers = {
            'x-rapidapi-key': "985371e109mshb5666c0424d5dcfp1b7485jsndf2afe5a3591",
            'x-rapidapi-host': "easy-instagramapi.p.rapidapi.com"
        }

        insta_response = requests.request(
            "GET", url, headers=headers
        ).json()

        with open(OUTFILE_LOCATION, 'w', encoding='utf8') as json_file:
            json_file.write(
                json.dumps(insta_response, indent=4, ensure_ascii=False)
            )

        print("Data successfully pulled from API...")

        # Post.objects.all().delete()
        #
        # print("Repopping Insta Data...")
        #
        # create_insta_data(OUTFILE_LOCATION)
        #
        # print("Successfully prepped Insta!")
