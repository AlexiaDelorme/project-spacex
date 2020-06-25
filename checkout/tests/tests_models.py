from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from checkout.models import (
    OtherPassenger,
    BookingReference
)
from trips.models import TripCategory, DepartureSite, Trip


class CheckoutModelsTests(TestCase):

    def setUp(self):

        # create dummy user and initialize session
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        self.client = Client()
        self.client.login(username='john', password='johnpassword')

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

        # create dummy instance of the booking reference object
        self.booking_1 = BookingReference.objects.create(
            booker=self.user,
            trip=self.trip_1,
            passenger_number=1,
        )

        # create dummy instance of the other passenger object
        self.passenger1 = OtherPassenger.objects.create(
            title='Mr',
            first_name='Jane',
            last_name='Doe',
            birth_month='November',
            birth_day='1',
            birth_year='1950',
            citizenship='France',
            passport_id='XXXXXX',
        )

    def test_other_passenger_str(self):
        expected_result = "Jane Doe"

        self.assertEqual(str(self.passenger1), expected_result)

    def test_other_passenger_birth_date_property(self):
        expected_result = "November 1, 1950"

        self.assertEqual(self.passenger1.birth_date, expected_result)

    def test_booking_reference_str(self):
        expected_result = "Ref: 1 - Moon - Kourou, France - 2020-07-15"

        self.assertEqual(str(self.booking_1), expected_result)
