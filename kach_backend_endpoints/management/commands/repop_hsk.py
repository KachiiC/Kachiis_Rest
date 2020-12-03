import os
from django.core.management.base import BaseCommand
from kach_backend_endpoints.backend_list.hsk_api.hsk_model import Word, HSKLevel
from kach_backend_endpoints.management.repoppers.hsk_repoppers import create_new_hsk_words


class Command(BaseCommand):
    def handle(self, *args, **options):
        Word.objects.all().delete()
        HSKLevel.objects.all().delete()

        create_new_hsk_words(os.getcwd() + '/kach_backend_endpoints/data/hsk/hskData.json')

        for x in range(1, 7):
            HSKLevel(
                level=x
            ).save()

        words = Word.objects.all()
        all_levels = HSKLevel.objects.all()

        for word in words:
            for hsk_level in all_levels:
                if word.hsk_level == hsk_level.level:
                    correct_level = HSKLevel.objects.get(level=word.hsk_level)
                    correct_level.words.add(word)

        print("HSK repop complete!")