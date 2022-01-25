from django.test import TestCase

# Create your tests here.

class ContactFormViewTest(TestCase):
    def test_get_contact_form_page(self):
        response = self.client.get('http://localhost:8000/contact/')
        self.assertEqual(response.status_code, 200)

    def test_get_successful_page(self):
        response = self.client.get('http://localhost:8000/contact/successful')
        self.assertEqual(response.status_code, 200)

    def test_get_unsuccessful_page(self):
        response = self.client.get('http://localhost:8000/contact/unsuccessful')
        self.assertEqual(response.status_code, 200)

    def test_post_to_contact_form_page(self):
        response  = self.client.post('http://localhost:8000/contact/', {'name': 'Steve', 'blah': 'blah@blah.com', 'phone_number': 1234567890})
        self.assertEqual(response.status_code, 200)
