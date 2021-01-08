import os
import csv
import json
from django.core.management.base import BaseCommand
from kach_backend_endpoints.backend_list.mma_techniques.mma_techniques_model import Technique
from kach_backend_endpoints.management.repoppers.mma_techniques_repoppers import create_mma_techniques

CSV_FILE = os.getcwd() + "/kach_backend_endpoints/data/mma_techniques/mma_techniques.csv"
JSON_OUTPUT = os.getcwd() + "/kach_backend_endpoints/data/mma_techniques/mmaTechniquesData.json"


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

        Technique.objects.all().delete()

        print("Repopping MMA techniques...")
        create_mma_techniques(os.getcwd() + '/kach_backend_endpoints/data/mma_techniques/mmaTechniquesData.json')

        print("MMA Techniques repop complete!")
