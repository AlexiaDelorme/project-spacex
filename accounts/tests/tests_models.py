from django.test import TestCase
from accounts.models import ContactDetail, Passenger
from django.contrib.auth.models import User


class TestContactModel(TestCase):

    def setUp(self):

        # create dummy instance of the contact object
        self.contact1 = ContactDetail.objects.create(
            user=User.objects.create_user(
                username='test',
                first_name='Test',
                last_name="User",
                email='test@test.com',
                password='12345678'
            ),
            phone_number='0033000000',
            street_address1='32 test street',
            postcode='1234',
            town_or_city='test city',
            country='France'
        )

    def test_contact_str(self):
        expected_result = "Test User"

        self.assertEqual(str(self.contact1), expected_result)

    def test_contact_full_name_property(self):
        expected_result = "Test User"

        self.assertEqual(self.contact1.full_name, expected_result)


class TestPassengerModel(TestCase):

    def setUp(self):

        # create dummy instance of the passenger object
        self.passenger1 = Passenger.objects.create(
            user=User.objects.create_user(
                username='test',
                first_name='Test',
                last_name="User",
                email='test@test.com',
                password='12345678'
            ),
            title='Mr',
            birth_month='November',
            birth_day='1',
            birth_year='1950',
            citizenship='France',
            passport_id='XXXXXX',
        )

    def test_passenger_str(self):
        expected_result = "Test User"

        self.assertEqual(str(self.passenger1), expected_result)

    def test_passenger_full_name_property(self):
        expected_result = "Test User"

        self.assertEqual(self.passenger1.full_name, expected_result)

    def test_passenger_birth_date_property(self):
        expected_result = "November 1, 1950"

        self.assertEqual(self.passenger1.birth_date, expected_result)
