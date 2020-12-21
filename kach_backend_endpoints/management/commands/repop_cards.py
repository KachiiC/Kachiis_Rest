import os
from django.core.management.base import BaseCommand
from kach_backend_endpoints.backend_list.cards_api.card_model import Card
from kach_backend_endpoints.management.repoppers.card_repoppers import create_new_cards


class Command(BaseCommand):
    def handle(self, *args, **options):
        Card.objects.all().delete()

        print("Old cards deleted")

        create_new_cards(os.getcwd() + '/kach_backend_endpoints/data/cards/cardData.json')

        print("Successfully repopped cards!")
