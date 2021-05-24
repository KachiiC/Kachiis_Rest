import os
import json
from kach_backend_endpoints.management.csv_converter import csv_converter
from django.core.management.base import BaseCommand
from kach_backend_endpoints.management.repoppers.mma_fighter_repoppers import create_mma_fighter
from kach_backend_endpoints.backend_list.mma_backend.mma_divisions.mma_divisions_model import Division
from kach_backend_endpoints.backend_list.mma_backend.mma_fighters.mma_fighter_model import Fighter

file_location = os.getcwd() + "/kach_backend_endpoints/data/mma_legends/"
CSV_FILE = file_location + "mma_legends.csv"
JSON_OUTPUT = file_location + "mmaLegends.json"

my_url = "https://www.ufc.com/athlete/"


class Command(BaseCommand):
    def handle(self, *args, **options):

        csv_converter(CSV_FILE,JSON_OUTPUT)
        print("conversion complete!")

        with open(JSON_OUTPUT, 'r') as json_file:
            fighter_data = json.load(json_file)

        for fighter in fighter_data:

            # grabbing page

            fighter_name = fighter["first_name"] + " " + fighter["last_name"]
            fighter_rank = 0
            division_name = fighter["weight_class"]

            # create_mma_fighter(fighter_name, fighter_rank, division_name)

            print(f"{fighter_name} created!")
            print(f"{fighter_name} created!")

        # Adds fighters to divisions
        # all_fighters = Fighter.objects.all()
        # all_divisions = Division.objects.all()
        # #
        # print("Adding fighters to correct divisions...")
        # for division in all_divisions:
        #     for fighter in all_fighters:
        #         if fighter.weight_class == division.weight_class:
        #             division.fighters.add(fighter)
        # print("All divisions added!")
        #
        # print("Repop Complete!")
