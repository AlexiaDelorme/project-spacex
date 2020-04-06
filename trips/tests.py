# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Trip

# Create your tests here.
class TripTests(TestCase):
       
    def test_str(self):
        test_destination = Trip(destination='A destination')
        self.assertEqual(str(test_destination), 'A destination')
