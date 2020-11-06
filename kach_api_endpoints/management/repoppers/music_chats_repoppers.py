import json
from kach_api_endpoints.api_list.music_chart_api.music_chart_model import Song


def create_new_music_chart(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)

    for song in data:
        print(song["artist"])