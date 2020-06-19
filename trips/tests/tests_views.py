from django.test import TestCase
from trips.models import Trip, TripCategory, DepartureSite
from trips.forms import TripSearchForm, AllTripSearchForm


class TestTripsPages(TestCase):

    def setUp(self):
        """Create a dummy instance of the trip object"""

        self.cat_1 = TripCategory.objects.create(
            title='Trip to the Moon',
            destination='Moon',
            destination_code='MNX',
            duration=1,
            distance=400000,
            price=10000,
            description='bla bla bla'
        )
        self.dep_site_1 = DepartureSite.objects.create(
            site_name='Kourou',
            country='French Guiana',
            site_code='CSG'
        )
        self.trip_1 = Trip.objects.create(
            category=self.cat_1, departure_site=self.dep_site_1,
            departure_date='2020-07-15', departure_time='06:00:00',
            return_time='12:00:00', slot='15'
        )

    def test_get_faq_page(self):

        response = self.client.get('/trips/faq/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq.html')

    def test_get_trips_categories_page(self):

        response = self.client.get('/trips/categories/')
        context = response.context

        self.assertEqual(response.status_code, 200)
        self.assertIn('page_title', context)
        self.assertIn('trip_categories', context)
        self.assertTemplateUsed(response, 'trips_categories.html')

    def test_get_trip_detail_page(self):

        url = "/trips/detail/" + str(self.cat_1.id) + "/"
        response = self.client.get(url)
        trip_form = response.context['form']

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trip_detail.html')
        self.assertEqual(type(trip_form), TripSearchForm)

    def test_post_results_page(self):

        url = "/trips/results/" + str(self.cat_1.id) + "/"
        form = {
            'departure_site': self.dep_site_1.id,
            'departure_date': self.trip_1.departure_date,
            'passenger_number': '1'
        }
        response = self.client.post(url, form)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trips_results.html')

    def test_get_all_trips_page(self):

        response = self.client.get('/trips/all/')
        trip_form = response.context['form']

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trips_all.html')
        self.assertEqual(type(trip_form), AllTripSearchForm)

    def test_post_all_trips_page(self):

        url = "/trips/all/"
        form = {
            'destination': self.cat_1.id,
            'departure_site': self.dep_site_1.id,
            'departure_date': self.trip_1.departure_date,
            'passenger_number': '1'
        }
        response = self.client.post(url, form)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trips_all.html')
