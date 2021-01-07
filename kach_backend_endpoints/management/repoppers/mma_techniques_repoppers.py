import json
from kach_backend_endpoints.backend_list.mma_techniques.mma_techniques_model import Technique


def create_mma_techniques(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)

        for technique in data:
            Technique(
                title=technique["title"],
                type=technique["type"],
                discipline=technique["discipline"],
                difficulty=technique["difficulty"],
                description=technique["description"],
                tutorial=technique["tutorial"],
                mistakes=technique["mistakes"]
            ).save()
