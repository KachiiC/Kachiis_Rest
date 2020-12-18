import json
from kach_static_pages.models import DisplayCard


def create_display_card(data_location):
    with open(data_location, 'r') as json_file:
        card_data = json.load(json_file)

        for data in card_data:
            DisplayCard(
                title=data["title"],
                description=data["description"],
                card_link=data["card_link"],
            ).save()
