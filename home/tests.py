from django.test import TestCase
from django.urls import reverse


class URLTests (TestCase):
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_contact_us(self):
        response = self.client.get(reverse('contact-us'))
        self.assertEqual(response.status_code, 200)

    def test_about_us(self):
        response = self.client.get(reverse('about-us'))
        self.assertEqual(response.status_code, 200)

    def test_membership(self):
        response = self.client.get(reverse('membership'))
        self.assertEqual(response.status_code, 200)
