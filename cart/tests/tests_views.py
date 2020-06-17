from django.test import TestCase, Client
from django.contrib.auth.models import User
from trips.models import Trip, TripCategory, DepartureSite


class TestCartViewPage(TestCase):

    def setUp(self):
        """Create a dummy instance of the User model """

        self.user = User.objects.create_user(
            username='test', email='test@test.com', password='12345678'
        )

    def test_get_cart_page(self):
        response = self.client.get('/cart/')
        session = self.client.session

        self.assertEqual(response.status_code, 200)
        self.assertNotIn('booking_references', session, msg=None)
        self.assertTemplateUsed(response, 'cart.html')

    def test_cart_page_session_logged_out(self):
        """Test that session variable 'referrer' is equal to checkout when user
        is logged out."""

        self.client.get('/cart/')
        session = self.client.session

        self.assertEqual(session['referrer'], 'checkout')

    def test_booking_references_session_variable(self):
        """Test booking_references session variable being deleted if it already
        exists in the view."""

        # manually sets booking_references session variable
        session = self.client.session
        session['booking_references'] = {'1': '1', '2': '2'}
        session.save()

        # check if session var being deleted when user gets to cart url
        self.client.get('/cart/')
        session = self.client.session

        self.assertNotIn('booking_references', session, msg=None)


class TestAddToCartView(TestCase):

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

    def test_add_to_cart(self):

        url = "/cart/add/" + str(self.trip_1.id) + "/"
        response = self.client.post(url, {'passenger': '2'})
        session = self.client.session
        expected_cart = {str(self.trip_1.id): 2}
        # messages = list(response.context['messages'])

        # add item to cart
        self.assertEqual(session['cart'], expected_cart)
        self.assertEqual(response.status_code,  302)
        self.assertEqual(response.url, "/cart/")
        # self.assertEqual(len(messages), 1)
        # self.assertEqual(str(messages[0]), 'This trip was added to your cart')

    def test_add_to_cart_if_not_empty(self):

        # manually sets cart session variable
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()

        # add item to cart and amend passenger number
        url = "/cart/add/" + str(self.trip_1.id) + "/"
        response = self.client.post(url, {'passenger': '3'})
        expected_cart = {str(self.trip_1.id): 3}
        session = self.client.session

        self.assertEqual(session['cart'], expected_cart)
        self.assertEqual(response.status_code,  302)
        self.assertEqual(response.url, "/cart/")


class TestAdjustCartView(TestCase):

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

    def test_adjust_cart(self):

        # manually sets cart session variable
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()

        # adjust passenger number in cart
        url = "/cart/adjust/" + str(self.trip_1.id) + "/"
        response = self.client.post(url, {'passenger': '3'})
        session = self.client.session
        expected_cart = {str(self.trip_1.id): 3}

        self.assertEqual(session['cart'], expected_cart)
        self.assertEqual(response.status_code,  302)
        self.assertEqual(response.url, "/cart/")

    def test_adjust_cart_passenger_equals_0(self):

        # manually sets cart session variable
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()

        # adjust passenger to 0
        url = "/cart/adjust/" + str(self.trip_1.id) + "/"
        response = self.client.post(url, {'passenger': '0'})
        session = self.client.session

        self.assertEqual(session['cart'], {})
        self.assertEqual(response.status_code,  302)
        self.assertEqual(response.url, "/cart/")

    def test_remove_from_cart(self):

        # manually sets cart session variable
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()

        # removes item from cart
        url = "/cart/remove/" + str(self.trip_1.id) + "/"
        response = self.client.post(url)
        session = self.client.session

        self.assertEqual(session['cart'], {})
        self.assertEqual(response.status_code,  302)
        self.assertEqual(response.url, "/cart/")
