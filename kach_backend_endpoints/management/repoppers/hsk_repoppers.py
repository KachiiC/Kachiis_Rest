import json
from kach_backend_endpoints.backend_list.hsk_api.hsk_model import Word


def create_new_hsk_words(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)

        for content in data:
            Word(
                chinese_characters=content["chinese_characters"],
                pinyin=content["pinyin"],
                type=content["type"],
                definition=content["definition"],
                hsk_level=content["hsk_level"]
            ).save()
