import os
import csv
import json
from django.core.management.base import BaseCommand
from kach_backend_endpoints.backend_list.mma_fights.mma_fights_model import Fight
from kach_backend_endpoints.backend_list.mma_fighters.mma_fighter_model import Fighter
from kach_backend_endpoints.management.repoppers.mma_fights_repoppers import create_mma_fights

File_Location = os.getcwd() + "/kach_backend_endpoints/data/mma_fights/"
CSV_FILE = File_Location + "mma_fights.csv"
JSON_OUTPUT = File_Location + "mmaFightsData.json"


class Command(BaseCommand):
    def handle(self, true=None, *args, **options):
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

        Fight.objects.all().delete()

        print("Repopping MMA fights...")
        create_mma_fights(JSON_OUTPUT)

        all_fighters = Fighter.objects.all()
        all_fights = Fight.objects.all()

        for fighter in all_fighters:
            full_name = fighter.first_name + " " + fighter.last_name

            for fight in all_fights:
                if fight.blue_corner == full_name or Fight.red_corner == full_name:
                    if fight.notable_win is True:
                        fighter.notable_wins.add(fight)

        print("MMA Fights repop complete!")
