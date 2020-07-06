from django.test import TestCase
from trips.models import (
    DepartureSite,
    RequiredDocument,
    TripImage,
    TripCategory,
    Trip
)


class TripTests(TestCase):

    def setUp(self):

        # create dummy instance of the trip object
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
            country='FR',
            site_code='CSG'
        )
        self.trip_1 = Trip.objects.create(
            category=self.cat_1, departure_site=self.dep_site_1,
            departure_date='2020-07-15', departure_time='06:00:00',
            return_time='12:00:00', slot='15'
        )

    def test_departure_site_str(self):
        self.assertEqual(str(self.dep_site_1), 'Kourou, France')

    def test_required_document_str(self):
        required_document = RequiredDocument(name='Passport')
        self.assertEqual(str(required_document), 'Passport')

    def test_trip_image_str(self):
        trip_image = TripImage(img_name='Moon 1')
        self.assertEqual(str(trip_image), 'Moon 1')

    def test_trip_category_str(self):
        self.assertEqual(str(self.cat_1), 'Moon')

    def test_trip_str(self):
        expected_result = 'Moon - Kourou, France - 2020-07-15'
        self.assertEqual(str(self.trip_1), expected_result)

    def test_trip_reference_property(self):
        self.assertEqual(self.trip_1.trip_reference, 'SPX1')
