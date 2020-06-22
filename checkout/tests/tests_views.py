from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.shortcuts import reverse
from accounts.models import ContactDetail, Passenger
from trips.models import TripCategory, Trip, DepartureSite
from accounts.forms import UserContactDetailForm, UserPassengerForm


class TestCheckoutContactViewPage(TestCase):

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
            country='French Guiana',
            site_code='CSG'
        )
        self.trip_1 = Trip.objects.create(
            category=self.cat_1, departure_site=self.dep_site_1,
            departure_date='2020-07-15', departure_time='06:00:00',
            return_time='12:00:00', slot='15'
        )

    def test_get_redirected_if_cart_empty_for_checkout_contact(self):
        response = self.client.get('/checkout/contact/')

        self.assertEqual(response.status_code,  302)
        self.assertEqual(response.url, reverse('view_cart'))

    def test_booking_references_session_variable(self):
        # set 'booking_references' and 'cart'
        session = self.client.session
        session['booking_references'] = {'1': '1'}
        session['cart'] = {'1': 1}
        session.save()
        # check if session var being deleted when user gets to url
        self.client.get('/checkout/contact/')
        session = self.client.session

        self.assertNotIn('booking_references', session, msg=None)

    def test_get_checkout_contact_page(self):
        # set cart
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()
        # get url
        response = self.client.get('/checkout/contact/')

        self.assertEqual(response.status_code,  200)
        self.assertTemplateUsed(response, 'checkout_contact.html')

    def test_post_contact_details_if_contact_does_not_exist(self):
        # set cart
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()
        # post url and form
        url = '/checkout/contact/'
        contact_form = {
            'phone_number': '+44 42 4242 4242',
            'street_address1': '125 Main St',
            'postcode': 'W1H7EJ',
            'town_or_city': 'London',
            'country': 'GB'
        }
        response = self.client.post(url, contact_form)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('checkout_passengers'))

    def test_form_in_context_if_contact_exists(self):
        # set contact details
        self.contact = ContactDetail.objects.create(
            user=self.user,
            phone_number='+44 65 6575 6575',
            street_address1='125 Main St',
            postcode='W1H7EJ',
            town_or_city='London',
            country='GB'
        )
        # set cart
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()
        # ger url
        response = self.client.get('/checkout/contact/')
        contact_form = response.context['form']

        self.assertEqual(type(contact_form), UserContactDetailForm)

    def test_post_contact_details_if_contact_exists(self):
        # set contact details
        self.contact = ContactDetail.objects.create(
            user=self.user,
            phone_number='+44 65 6575 6575',
            street_address1='125 Main St',
            postcode='W1H7EJ',
            town_or_city='London',
            country='GB'
        )
        # set cart
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()
        # post url and form
        url = '/checkout/contact/'
        contact_form = {
            'phone_number': '+44 424 4242 4242',
            'street_address1': '125 Union Square',
            'postcode': '00000',
            'town_or_city': 'Reading',
            'country': 'GB'
        }
        response = self.client.post(url, contact_form)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('checkout_passengers'))


class TestCheckoutPassengersViewPage(TestCase):

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
            country='French Guiana',
            site_code='CSG'
        )
        self.trip_1 = Trip.objects.create(
            category=self.cat_1, departure_site=self.dep_site_1,
            departure_date='2020-07-15', departure_time='06:00:00',
            return_time='12:00:00', slot='15'
        )

    def test_get_redirected_if_cart_empty_for_checkout_passengers(self):
        response = self.client.get('/checkout/passengers/')

        self.assertEqual(response.status_code,  302)
        self.assertEqual(response.url, reverse('view_cart'))

    def test_get_checkout_passengers_page(self):
        # set cart
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()
        # get url
        response = self.client.get('/checkout/passengers/')

        self.assertEqual(response.status_code,  200)
        self.assertTemplateUsed(response, 'checkout_passengers.html')

    def test_form_in_context_if_passenger_exists(self):
        # set passenger details
        self.passenger = Passenger.objects.create(
            user=self.user,
            title='Mr',
            birth_month='October',
            birth_day='9',
            birth_year='1940',
            citizenship='GB',
            passport_id='UK00000'
        )
        # set cart
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()
        # ger url
        response = self.client.get('/checkout/passengers/')
        form = response.context['form']

        self.assertEqual(type(form), UserPassengerForm)


class TestCheckoutConfirmationViewPage(TestCase):

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
            country='French Guiana',
            site_code='CSG'
        )
        self.trip_1 = Trip.objects.create(
            category=self.cat_1, departure_site=self.dep_site_1,
            departure_date='2020-07-15', departure_time='06:00:00',
            return_time='12:00:00', slot='15'
        )

    def test_get_redirected_if_cart_empty_for_checkout_confirmation(self):
        response = self.client.get('/checkout/confirmation/')

        self.assertEqual(response.status_code,  302)
        self.assertEqual(response.url, reverse('view_cart'))

    def test_get_checkout_confirmation_page(self):
        # set cart
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()
        # get url
        response = self.client.get('/checkout/confirmation/')

        self.assertEqual(response.status_code,  200)
        self.assertTemplateUsed(response, 'checkout_confirmation.html')
