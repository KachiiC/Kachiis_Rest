import json
from kach_api_endpoints.api_list.imdb_api.imdb_model import Content


def create_tv_imdb_data(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)

        for content in data[0]["tv_results"]:
            Content(
                title=content["title"],
                imdb_id=content["imdb_id"],
                content_type=data[1]["name"],
                media_type="TV shows",
                released=int(content["year"]),
            ).save()


def create_movie_imdb_data(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)

        for content in data[0]["movie_results"]:
            Content(
                title=content["title"],
                imdb_id=content["imdb_id"],
                content_type=data[1]["name"],
                media_type="Movies",
                released=int(content["year"]),
            ).save()
