import json
from django.test import TestCase
from rest_framework.test import APITestCase


# Create your tests here.
class SWAPITestCases(APITestCase):
    """
    Test cases for list planets and movies api.
    """

    def test_list_planets(self):
        response = self.client.get('/api/planets')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['results'][0]['name'], 'Alderaan')

        response = self.client.get('/api/planets', {'search': 'yavin'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['results'][0]['name'], 'Yavin IV')

    def test_list_movies(self):
        response = self.client.get('/api/movies')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['results'][0]['title'], 'A New Hope')

        response = self.client.get('/api/movies', {'search': 'hope'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['results'][0]['title'], 'A New Hope')
