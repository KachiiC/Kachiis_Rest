from django.core.management.base import BaseCommand
from kach_backend_endpoints.management.url_webscrapper import url_webscraper
from kach_backend_endpoints.backend_list.mma_backend.mma_store.mma_store_model import StoreItem

my_url = "https://uk.venum.com/gb/new-arrivals.html"


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Delete all objects
        StoreItem.objects.all().delete()

        # Grabs Articles
        page = url_webscraper(my_url)

        all_items = page.findAll("li", "item product product-item")
        # Slice to only 12 items
        items_slice = slice(0, 12)
        latest_items = all_items[items_slice]

        for item in latest_items:
            StoreItem(
                name=item.img["src"],
                price=item.find("span", "price").text.strip()[1:],
                product_thumbnail=item.find("a", "product-item-link").text.strip(),
                product_link=item.find("a", "product-item-link")["href"],
            ).save()

        print("store repop complete!")
