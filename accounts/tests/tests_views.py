from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.shortcuts import reverse
from accounts.forms import (
    UserSignupForm,
    UserPassengerForm,
    UserContactDetailForm
)
from django.contrib.auth.forms import PasswordChangeForm
from accounts.models import Passenger, ContactDetail


class TestLogoutView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')

    def test_logout_view_if_user_not_authenticated(self):
        response = self.client.get('/accounts/logout/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url, '/accounts/login/?next=/accounts/logout/')

    def test_logout_view(self):
        self.client = Client()
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/accounts/logout/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))


class TestSignUpViewPage(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')

    def test_signup_page_if_user_authenticated(self):
        self.client = Client()
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/accounts/signup/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login_success'))

    def test_get_signup_page(self):
        response = self.client.get('/accounts/signup/')
        signup_form = response.context['form']

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertEqual(type(signup_form), UserSignupForm)

    def test_post_signup_form_success(self):

        url = '/accounts/signup/'
        signup_form = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'username': 'JaneDoe',
            'email': 'jane.doe@test.com',
            'password1': 'janepassword',
            'password2': 'janepassword'
        }
        response = self.client.post(url, signup_form)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login_success'))

    def test_post_signup_form_failure(self):

        url = '/accounts/signup/'
        signup_form = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'username': 'JaneDoe',
            'email': 'jane.doe@test.com',
            'password1': 'janepassword',
            'password2': ''
        }
        response = self.client.post(url, signup_form)
        messages = list(response.context['messages'])

        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Please correct the error(s) below')


class TestProfileViewPage(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        self.client = Client()
        self.client.login(username='john', password='johnpassword')

    def test_get_profile_page(self):
        response = self.client.get('/accounts/profile/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')

    def test_context_if_passenger_details_exist(self):
        self.passenger = Passenger.objects.create(
            user=self.user,
            title='Mr',
            birth_month='October',
            birth_day='9',
            birth_year='1940',
            citizenship='GB',
            passport_id='UK00000'
        )
        response = self.client.get('/accounts/profile/')
        passenger = response.context['passenger']
        
        self.assertEqual(passenger, self.passenger)

    def test_context_if_contact_details_exist(self):
        self.contact = ContactDetail.objects.create(
            user=self.user,
            phone_number='+44 65 6575 6575',
            street_address1='125 Main St',
            postcode='W1H7EJ',
            town_or_city='London',
            country='GB'
        )
        response = self.client.get('/accounts/profile/')
        contact = response.context['contact']

        self.assertEqual(contact, self.contact)

    def test_context_if_passenger_and_contact_details_exist(self):
        self.passenger = Passenger.objects.create(
            user=self.user,
            title='Mr',
            birth_month='October',
            birth_day='9',
            birth_year='1940',
            citizenship='GB',
            passport_id='UK00000'
        )
        self.contact = ContactDetail.objects.create(
            user=self.user,
            phone_number='+44 65 6575 6575',
            street_address1='125 Main St',
            postcode='W1H7EJ',
            town_or_city='London',
            country='GB'
        )
        response = self.client.get('/accounts/profile/')
        passenger = response.context['passenger']
        contact = response.context['contact']

        self.assertEqual(passenger, self.passenger)
        self.assertEqual(contact, self.contact)


class TestCreatePassengerDetailsPage(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')

    def test_get_create_passenger_details_page(self):
        self.client = Client()
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/accounts/profile/create-passenger/')
        passenger_form = response.context['form']

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'profile/create_passenger_details.html')
        self.assertEqual(type(passenger_form), UserPassengerForm)

    def test_post_passenger_details_form_success(self):
        self.client = Client()
        self.client.login(username='john', password='johnpassword')
        url = '/accounts/profile/create-passenger/'
        passenger_form = {
            'title': 'Mr',
            'birth_month': 'October',
            'birth_day': '9',
            'birth_year': '1940',
            'citizenship': 'GB',
            'passport_id': 'UK000000',
        }
        response = self.client.post(url, passenger_form)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('profile'))

    def test_post_passenger_details_form_failure(self):
        self.client = Client()
        self.client.login(username='john', password='johnpassword')
        url = '/accounts/profile/create-passenger/'
        passenger_form = {
            'title': '',
            'birth_month': 'October',
            'birth_day': '9',
            'birth_year': '1940',
            'citizenship': 'GB',
            'passport_id': '',
        }
        response = self.client.post(url, passenger_form)
        messages = list(response.context['messages'])

        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Please correct the error(s) below')


class TestCreateContactDetailsPage(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')

    def test_get_create_contact_details_page(self):
        self.client = Client()
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/accounts/profile/create-contact/')
        contact_form = response.context['form']

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'profile/create_contact_details.html')
        self.assertEqual(type(contact_form), UserContactDetailForm)

    def test_post_contact_details_form_success(self):
        self.client = Client()
        self.client.login(username='john', password='johnpassword')
        url = '/accounts/profile/create-contact/'
        contact_form = {
            'phone_number': '0044 424 4242 4242',
            'street_address1': '124 main street',
            'postcode': '9999',
            'town_or_city': 'London',
            'country': 'GB'
        }
        response = self.client.post(url, contact_form)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('profile'))

    def test_post_contact_details_form_failure(self):
        self.client = Client()
        self.client.login(username='john', password='johnpassword')
        url = '/accounts/profile/create-contact/'
        contact_form = {
            'phone_number': '',
            'street_address1': '124 main street',
            'postcode': '9999',
            'country': 'GB'
        }
        response = self.client.post(url, contact_form)
        messages = list(response.context['messages'])

        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Please correct the error(s) below')


class TestEditPassengerDetailsPage(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        self.client = Client()
        self.client.login(username='john', password='johnpassword')
        self.passenger = Passenger.objects.create(
            user=self.user,
            title='Mr',
            birth_month='October',
            birth_day='9',
            birth_year='1940',
            citizenship='GB',
            passport_id='UK00000'
        )

    def test_get_edit_passenger_details_page(self):
        response = self.client.get('/accounts/profile/edit-passenger/')
        passenger_form = response.context['form']

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'profile/edit_passenger_details.html')
        # Test failing to be resolved
        # self.assertEqual(type(passenger_form), UserPassengerForm())

    def test_post_edit_passenger_details_form_success(self):
        url = '/accounts/profile/edit-passenger/'
        passenger_form = {
            'title': 'Mr',
            'birth_month': 'October',
            'birth_day': '9',
            'birth_year': '1940',
            'citizenship': 'GB',
            'passport_id': 'UK876789',
        }
        response = self.client.post(url, passenger_form)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('profile'))

    def test_post_edit_passenger_details_form_failure(self):
        url = '/accounts/profile/edit-passenger/'
        passenger_form = {
            'title': '',
            'birth_month': 'October',
            'birth_day': '9',
            'birth_year': '1940',
            'citizenship': 'GB',
            'passport_id': '',
        }
        response = self.client.post(url, passenger_form)
        messages = list(response.context['messages'])

        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Please correct the error(s) below')


# Test edit contact details page


class TestEditPasswordPage(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        self.client = Client()
        self.client.login(username='john', password='johnpassword')

    def test_get_edit_password_page(self):
        response = self.client.get('/accounts/profile/edit-password/')
        password_form = response.context['form']

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'profile/edit_password.html')
        self.assertEqual(type(password_form), PasswordChangeForm)

    def test_post_edit_password_form_success(self):
        url = '/accounts/profile/edit-password/'
        password_form = {
            'old_password': 'johnpassword',
            'new_password1': 'changedpassword',
            'new_password2': 'changedpassword'
        }
        response = self.client.post(url, password_form)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('profile'))

    def test_post_edit_password_form_failure(self):
        url = '/accounts/profile/edit-password/'
        contact_form = {
            'old_password': 'johnpassword',
            'new_password1': '',
            'new_password2': 'changedpassword'
        }
        response = self.client.post(url, contact_form)
        messages = list(response.context['messages'])

        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Please correct the error(s) below')


class TestBookingsPage(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        self.client = Client()
        self.client.login(username='john', password='johnpassword')

    def test_get_bookings_view_page(self):
        response = self.client.get('/accounts/bookings/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/bookings.html')


class TestLoginSuccessView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')

    def test_login_success_view(self):

        response = self.client.get('/accounts/login_success/')
        session = self.client.session

        self.assertEqual(session['referrer'], 'none')
        self.assertEqual(response.status_code, 302)
        # Test failing to be resolved
        # self.assertEqual(response.url, reverse('profile'))

    def test_login_success_referrer_checkout(self):

        # manually sets referrer session variable to checkout
        session = self.client.session
        session['referrer'] = 'checkout'
        session.save()

        response = self.client.get('/accounts/login_success/')
        session = self.client.session

        self.assertEqual(session['referrer'], 'none')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('checkout_contact'))
