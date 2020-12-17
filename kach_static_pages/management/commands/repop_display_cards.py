import os
from django.core.management.base import BaseCommand
from kach_static_pages.models import DisplayCard
from kach_static_pages.management.repoppers.display_cards_repoppers import create_display_card


class Command(BaseCommand):
    def handle(self, *args, **options):
        DisplayCard.objects.all().delete()

        create_display_card(os.getcwd() + "/kach_static_pages/data/display_cards.json")
        print("repopping display cards successful")
