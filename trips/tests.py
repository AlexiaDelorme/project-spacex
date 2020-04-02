# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Trip

# Create your tests here.
class TripTests(TestCase):
       
    def test_str(self):
        test_title = Trip(title='A trip')
        self.assertEqual(str(test_title), 'A trip')
