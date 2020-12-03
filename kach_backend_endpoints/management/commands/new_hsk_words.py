from django.core.management.base import BaseCommand
from kach_backend_endpoints.backend_list.hsk_api.hsk_model import HSKLevel


class Command(BaseCommand):
    def handle(self, *args, **options):

        HSKLevel.objects.all().delete()

        for x in range(1, 7):
            HSKLevel(
                level=x
            ).save()

        print("new levels made")
