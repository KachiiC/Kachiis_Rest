from django.core.management.base import BaseCommand
import os
# Models
from kach_api_endpoints.api_list.music_chart_api.music_chart_model import Song
from kach_api_endpoints.management.repoppers.music_chats_repoppers import create_new_music_chart

MUSIC_CHART_DATA_DIR = os.getcwd() + "/kach_api_endpoints/data/music_charts/music_charts.json"


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Deletes all songs and repopulates Model with songs from prep_music_charts"""
        Song.objects.all().delete()

        create_new_music_chart(MUSIC_CHART_DATA_DIR)
        print("repop successful")
