from django.test import TestCase
from django.urls import reverse


class URLTests (TestCase):
    def test_cart(self):
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)
