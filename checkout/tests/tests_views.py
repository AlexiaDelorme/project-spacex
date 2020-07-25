from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.shortcuts import reverse
from accounts.models import ContactDetail, Passenger
from trips.models import TripCategory, Trip, DepartureSite
from checkout.models import BookingReference, OtherPassenger
from accounts.forms import UserContactDetailForm, UserPassengerForm
from checkout.forms import PaymentForm


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

    def test_post_form_if_contact_does_not_exist(self):

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

    def test_post_incorrect_form_if_contact_does_not_exist(self):

        # set cart
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()

        # post url and incorrect form
        url = '/checkout/contact/'
        contact_form = {
            'town_or_city': 'London',
            'country': 'GB'
        }
        response = self.client.post(url, contact_form)
        messages = list(response.context['messages'])

        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Please correct the error(s) below')

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

    def test_post_form_if_contact_exists(self):

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

    def test_post_incorrect_form_if_contact_exists(self):

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

        # post url and incorrect form
        url = '/checkout/contact/'
        contact_form = {
            'town_or_city': 'Brixton',
            'country': 'GB'
        }
        response = self.client.post(url, contact_form)
        messages = list(response.context['messages'])

        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Please correct the error(s) below')


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


class TestSavePassengersViews(TestCase):

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

        # create dummy instance of the booking reference object
        self.booking_1 = BookingReference.objects.create(
            booker=self.user,
            trip=self.trip_1,
            passenger_number=1,
        )

    def test_save_other_passenger(self):

        # set 'booking_references'
        session = self.client.session
        session['booking_references'] = {
            str(self.trip_1.id): str(self.booking_1.id)}
        session.save()

        # set url and post form
        url = "/checkout/save-passenger/" + str(self.trip_1.id) + "/"
        other_passenger_form = {
            'title': 'Mrs',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'birth_month': 'January',
            'birth_day': '1',
            'birth_year': '1980',
            'citizenship': 'GB',
            'passport_id': 'UK00000',
        }
        response = self.client.post(url, other_passenger_form)
        passenger = OtherPassenger.objects.filter(
            first_name='Jane', last_name='Doe').first()

        self.assertEqual(response.status_code,  302)
        self.assertEqual(response.url, reverse('checkout_passengers'))
        self.assertIsInstance(passenger, OtherPassenger)

    def test_save_user_passenger_if_passenger_does_not_exist(self):

        # set 'booking_references'
        session = self.client.session
        session['booking_references'] = {
            str(self.trip_1.id): str(self.booking_1.id)}
        session.save()

        # set url and post form
        url = "/checkout/save-user-passenger/" + str(self.trip_1.id) + "/"
        user_passenger_form = {
            'title': 'Mr',
            'birth_month': 'October',
            'birth_day': '9',
            'birth_year': '1940',
            'citizenship': 'GB',
            'passport_id': 'UK00000',
        }
        response = self.client.post(url, user_passenger_form)
        passenger = Passenger.objects.filter(id=self.user.id).first()

        self.assertEqual(response.status_code,  302)
        self.assertEqual(response.url, reverse('checkout_passengers'))
        self.assertIsInstance(passenger, Passenger)

    def test_save_user_passenger_if_passenger_exists(self):

        # create passenger instance
        self.passenger = Passenger.objects.create(
            user=self.user,
            title='Mr',
            birth_month='January',
            birth_day='9',
            birth_year='1940',
            citizenship='GB',
            passport_id='UKXXXXX'
        )

        # set 'booking_references'
        session = self.client.session
        session['booking_references'] = {
            str(self.trip_1.id): str(self.booking_1.id)}
        session.save()

        # set url and post form
        url = "/checkout/save-user-passenger/" + str(self.trip_1.id) + "/"
        user_passenger_form = {
            'title': 'Mr',
            'birth_month': 'October',
            'birth_day': '9',
            'birth_year': '1940',
            'citizenship': 'GB',
            'passport_id': 'UK00000',
        }
        self.client.post(url, user_passenger_form)
        passenger = Passenger.objects.filter(id=self.user.id).first()

        self.assertEqual('UK00000', passenger.passport_id)
        self.assertEqual('October', passenger.birth_month)


class TestCheckoutPaymentViewPage(TestCase):

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

        # create dummy instance of the booking reference object
        self.booking_1 = BookingReference.objects.create(
            booker=self.user,
            trip=self.trip_1,
            passenger_number=1,
        )

    def test_get_redirected_if_cart_empty_for_checkout_payment(self):
        response = self.client.get('/checkout/payment/')

        self.assertEqual(response.status_code,  302)
        self.assertEqual(response.url, reverse('view_cart'))

    def test_get_checkout_payment_page(self):

        # set cart
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()

        # get url
        response = self.client.get('/checkout/payment/')
        payment_form = response.context['form']

        self.assertEqual(type(payment_form), PaymentForm)

        self.assertEqual(response.status_code,  200)
        self.assertTemplateUsed(response, 'checkout_payment.html')

    def test_post_payment_form_failure(self):

        # set cart
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()

        # set url and post payment form
        url = '/checkout/payment/'
        payment_form = {
            'credit_card_number': '4242424242424242',
            'cvv': '000',
            'expiry_month': '',
            'expiry_year': '2019'
        }
        response = self.client.post(url, payment_form)
        messages = list(response.context['messages'])

        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'We were unable to take a payment with that card')


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

        # create dummy instance of the booking reference object
        self.booking_1 = BookingReference.objects.create(
            booker=self.user,
            trip=self.trip_1,
            passenger_number=1,
        )

        # set 'booking_references' session var
        session = self.client.session
        session['booking_references'] = {
            str(self.trip_1.id): str(self.booking_1.id)}
        session.save()

    def test_get_checkout_confirmation_page(self):

        response = self.client.get('/checkout/confirmation/')

        self.assertEqual(response.status_code,  200)
        self.assertTemplateUsed(response, 'checkout_confirmation.html')

    def test_booking_references_session_variable_is_deleted(self):

        self.client.get('/checkout/confirmation/')
        session = self.client.session

        self.assertNotIn('booking_references', session, msg=None)

    def test_bookings_variable_is_in_context(self):

        response = self.client.get('/checkout/confirmation/')

        self.assertIn('bookings', response.context)
        self.assertEqual(response.context['bookings'], [self.booking_1])
