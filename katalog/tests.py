from django.test import TestCase
from katalog.models import CatalogItem

# Create your tests here.
class KatalogTestCase(TestCase):
    def setUp(self):
        CatalogItem.objects.create(item_name = "Bakso", item_price = 5000, item_stock = 20, item_url = "https://www.tokopedia.com/", rating = 5, description = "bakso gaming")
        CatalogItem.objects.create(item_name = "Oskab", item_price = 15000, item_stock = 1, item_url = "https://www.tokopedia.com/", rating = 10, description = "bakso juga")

    def test_Katalogs_can_speak(self):
        bakso = CatalogItem.objects.get(item_name="Bakso")
        oskab = CatalogItem.objects.get(item_name="Oskab")

        self.assertEqual(bakso.item_name, "Bakso")
        self.assertEqual(oskab.item_price, 15000)