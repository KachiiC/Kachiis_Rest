import os
import json
import csv
from django.core.management.base import BaseCommand
from kach_backend_endpoints.management.url_webscrapper import url_webscraper
from kach_backend_endpoints.management.repoppers.mma_p4p_repopper import create_mma_p4p
from kach_backend_endpoints.backend_list.mma_backend.mma_divisions.mma_divisions_model import Division
from kach_backend_endpoints.backend_list.mma_backend.mma_fighters.mma_fighter_model import Fighter
from kach_backend_endpoints.management.repoppers.mma_fighter_repoppers import create_mma_fighter
from kach_backend_endpoints.backend_list.mma_backend.mma_dictionary.mma_dictionary_model import Dictionary
from kach_backend_endpoints.management.repoppers.mma_dictionary_repoppers import create_mma_dictionary

file_location = os.getcwd() + "/kach_backend_endpoints/data/mma_legends/"
CSV_FILE = file_location + "mma_legends.csv"
JSON_OUTPUT = file_location + "mmaLegends.json"

my_url = "https://www.ufc.com/athlete/"


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

        print("conversion complete!")

        with open(JSON_OUTPUT, 'r') as json_file:
            fighter_data = json.load(json_file)

        for fighter in fighter_data:

            # grabbing page

            fighter_name = fighter["first_name"] + " " + fighter["last_name"]
            fighter_rank = 0
            division_name = fighter["weight_class"]

            create_mma_fighter(fighter_name, fighter_rank, division_name)

            print("Legend Created!")

        # # Adds fighters to divisions
        # all_fighters = Fighter.objects.all()
        # all_divisions = Division.objects.all()
        #
        # print("Adding fighters to correct divisions...")
        # for division in all_divisions:
        #     for fighter in all_fighters:
        #         if fighter.weight_class == division.weight_class:
        #             division.fighters.add(fighter)
        # print("All divisions added!")
        #
        # print("Adding fighters to p4p_list...")
        # pound_for_pound_tables = [0, 9]
        #
        # for division in pound_for_pound_tables:
        #     create_mma_p4p(rankings[division])
        # print("p4p division added!")
        #
        # print("Repop Complete!")
