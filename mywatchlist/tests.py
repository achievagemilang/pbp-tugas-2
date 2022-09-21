from django.test import TestCase, Client

# Create your tests here.
class WatchlistTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_html(self):
        res = self.client.get('/mywatchlist/html/')
        self.assertEqual(res.status_code, 200)

    def test_get_xml(self):
        res = self.client.get('/mywatchlist/xml/')
        self.assertEqual(res.status_code, 200)

    def test_get_json(self):
        res = self.client.get('/mywatchlist/json/')
        self.assertEqual(res.status_code, 200)