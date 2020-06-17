from django.test import TestCase, Client
from trips.models import Trip, TripCategory, DepartureSite


class TestFaqPage(TestCase):

    def test_get_faq_page(self):
        response = self.client.get('/trips/faq/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq.html')


class TestTripsCategoriesPage(TestCase):

    def test_get_trips_categories_page(self):
        response = self.client.get('/trips/categories/')
        context = response.context

        self.assertEqual(response.status_code, 200)
        self.assertIn('page_title', context)
        self.assertIn('trip_categories', context)
        self.assertTemplateUsed(response, 'trips_categories.html')
