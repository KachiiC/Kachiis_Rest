import os
from django.core.management.base import BaseCommand
from kach_backend_endpoints.backend_list.mma_dictionary.mma_dictionary_model import Dictionary
from kach_backend_endpoints.management.repoppers.mma_dictionary_repoppers import create_mma_dictionary


class Command(BaseCommand):
    def handle(self, *args, **options):
        Dictionary.objects.all().delete()

        print("Repopping MMA words...")
        create_mma_dictionary(os.getcwd() + '/kach_backend_endpoints/data/mma_dictionary/mmaDictionaryData.json')

        print("MMA words repop complete!")