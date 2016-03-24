from django.test import TestCase
from parkpedia.models import Park
import sys, os

# directory to outer parkpedia_project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEST_PATH = os.path.join(BASE_DIR, 'load_data_test.py')


class ParkTestCase(TestCase):
    def setUp(self):
        execfile(TEST_PATH)

    def test_parse_data(self):
        minoru = Park.objects.get(parkId=1)
        self.assertEqual(minoru.name, "Minoru Park")
        self.assertEqual(minoru.parkId, 1)
        self.assertEqual(minoru.facilities, " | Playgrounds | Soccer Field")
        self.assertEqual(minoru.streetNum, 4202)
        self.assertEqual(minoru.streetName, "Valley Drive")
        self.assertEqual(minoru.washroom, "No")
        self.assertEqual(minoru.latLon, "49.249783,-123.155250")

        richmond = Park.objects.get(parkId=2)
        self.assertEqual(richmond.name, "Richmond Park")
        self.assertEqual(richmond.facilities, "None")


