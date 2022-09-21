from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class WatchlistTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_get_html(self):
        res = self.client.get(reverse('mywatchlist:show_mywatchlist'))
        self.assertEqual(res.status_code, 200)

    def test_get_xml(self):
        res = self.client.get(reverse('mywatchlist:show_mywatchlist_xml'))
        self.assertEqual(res.status_code, 200)

    def test_get_json(self):
        res = self.client.get(reverse('mywatchlist:show_mywatchlist_json'))
        self.assertEqual(res.status_code, 200)