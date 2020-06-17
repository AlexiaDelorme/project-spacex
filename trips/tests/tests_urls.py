from django.test import SimpleTestCase
from django.urls import reverse, resolve
from trips.views import (
    faq_page,
    trips_categories_page,
    trip_detail_page,
    trips_results_page,
    trips_all_page
)


class TestTripsUrls(SimpleTestCase):

    def test_faq_url_resolves(self):
        url = reverse('faq')
        self.assertEquals(resolve(url).func, faq_page)

    def test_trips_categories_url_resolves(self):
        url = reverse('trips_categories')
        self.assertEquals(resolve(url).func, trips_categories_page)

    def test_trips_details_url_resolves(self):
        url = reverse('trip_detail', args=['1'])
        self.assertEquals(resolve(url).func, trip_detail_page)

    def test_trips_results_url_resolves(self):
        url = reverse('trips_results', args=['1'])
        self.assertEquals(resolve(url).func, trips_results_page)

    def test_trips_all_url_resolves(self):
        url = reverse('trips_all')
        self.assertEquals(resolve(url).func, trips_all_page)
