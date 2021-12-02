from django.test import TestCase
from django.urls import reverse
from .models import GymClass, Trainer


class URLTests (TestCase):
    def setUp(self):
        GymClass.objects.create(
            name="test",
            description="test",
            level="test",
            duration=10,
            period=12,
            students=12,
            price=12
            )

        Trainer.objects.create(name="test", bio="test")

    def test_gym_classes(self):
        response = self.client.get(reverse('gym_classes'))
        self.assertEqual(response.status_code, 200)

    def test_gym_class(self):
        response = self.client.get(reverse('gym_class', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_trainers(self):
        response = self.client.get(reverse('trainers'))
        self.assertEqual(response.status_code, 200)

    def test_trainer(self):
        response = self.client.get(reverse('trainer', args=[1]))
        self.assertEqual(response.status_code, 200)
