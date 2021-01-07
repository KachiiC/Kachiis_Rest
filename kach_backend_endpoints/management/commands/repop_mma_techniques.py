import os
from django.core.management.base import BaseCommand
from kach_backend_endpoints.backend_list.mma_techniques.mma_techniques_model import Technique
from kach_backend_endpoints.management.repoppers.mma_techniques_repoppers import create_mma_techniques


class Command(BaseCommand):
    def handle(self, *args, **options):
        Technique.objects.all().delete()

        print("Repopping MMA techniques...")
        create_mma_techniques(os.getcwd() + '/kach_backend_endpoints/data/mma_techniques/mmaTechniquesData.json')

        print("MMA Techniques repop complete!")
