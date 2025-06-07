from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class CustomerTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/api/v1/customers/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location(self):
        response = self.client.get("api/v1/paypal/process/")
        self.assertEqual(response.status_code, 404)  # Method Not Allowed for GET requests
