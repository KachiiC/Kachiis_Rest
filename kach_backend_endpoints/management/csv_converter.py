import csv
import json


def csv_converter(csv_file, json_output):
    file_array = []

    with open(csv_file, encoding='utf-8') as csvf:
        csvreader = csv.DictReader(csvf)

        print("converting csv to json..")

        for row in csvreader:
            file_array.append(row)

        with open(json_output, 'w', encoding='utf-8') as jsonf:
            json_string = json.dumps(file_array, indent=4)
            jsonf.write(json_string)
