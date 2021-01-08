import json
from kach_backend_endpoints.backend_list.mma_dictionary.mma_dictionary_model import Dictionary


def create_mma_dictionary(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)

        for term in data:
            Dictionary(
                title=term["title"],
                type=term["type"],
                example=term["example"],
                example_type=term["example_type"],
                definition=term["definition"]
            ).save()
