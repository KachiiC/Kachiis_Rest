import os
import json
import csv
from django.core.management.base import BaseCommand
from kach_backend_endpoints.backend_list.mma_dictionary.mma_dictionary_model import Dictionary
from kach_backend_endpoints.management.repoppers.mma_dictionary_repoppers import create_mma_dictionary

CSV_FILE = os.getcwd() + "/kach_backend_endpoints/data/mma_dictionary/mma_dictionary.csv"
JSON_OUTPUT = os.getcwd() + "/kach_backend_endpoints/data/mma_dictionary/mmaDictionaryData.json"


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_array = []

        with open(CSV_FILE, encoding='utf-8') as csvf:
            csvreader = csv.DictReader(csvf)

            print("converting csv to json..")

            for row in csvreader:
                file_array.append(row)

            with open(JSON_OUTPUT, 'w', encoding='utf-8') as jsonf:
                json_string = json.dumps(file_array, indent=4)
                jsonf.write(json_string)

            print("conversion complete")

        Dictionary.objects.all().delete()

        print("Repopping MMA words...")
        create_mma_dictionary(JSON_OUTPUT)

        print("MMA words repop complete!")
