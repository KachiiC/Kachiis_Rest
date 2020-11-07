from django.core.management.base import BaseCommand
import os
# Models
from kach_api_endpoints.api_list.imdb_api.imdb_model import Content, ImdbList
from kach_api_endpoints.management.repoppers.imdb_repoppers import create_tv_imdb_data, create_movie_imdb_data

IMDB_DATA_DIR = os.getcwd() + "/kach_api_endpoints/data/imdb/"

content_types = ["popular", "trending"]


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Deletes all songs and repopulates Model with songs from prep_music_charts"""
        Content.objects.all().delete()
        ImdbList.objects.all().delete()

        for content in content_types:
            create_tv_imdb_data(IMDB_DATA_DIR + f"{content}_tv_shows.json")
            create_movie_imdb_data(IMDB_DATA_DIR + f"{content}_movies.json")
            print(f"{content} repop successful")

            ImdbList(
                list_title=f"{content} tv shows",
                content_type=f"{content}_tv_shows",
                media_type="TV shows"
            ).save()

            ImdbList(
                list_title=f"{content} movies",
                content_type=f"{content}_movies",
                media_type="Movies"
            ).save()

            print(f"{content} list created successfully")

        all_content = Content.objects.all()
        all_imdb_list = ImdbList.objects.all()

        for media in all_content:
            for imdb_list in all_imdb_list:
                if media.content_type == imdb_list.content_type:
                    correct_list = ImdbList.objects.get(content_type=media.content_type)
                    correct_list.content.add(media)
