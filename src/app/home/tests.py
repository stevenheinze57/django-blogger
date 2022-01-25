from django.test import TestCase

# Create your tests here.

class HomePageViewTest(TestCase):
    def test_get_home_page(self):
        response_http = self.client.get('http://localhost:8000/')
        response_https = self.client.get('https://localhost:8000/')
        response_home = self.client.get('https://localhost:8000/home/')
        self.assertEqual(response_http.status_code, 200)
        self.assertEqual(response_https.status_code, 200)
        self.assertEqual(response_home.status_code, 200)
