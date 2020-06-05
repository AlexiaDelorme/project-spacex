from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import (
    logout_page,
    signup_page,
    profile_page,
    create_passenger_details_page,
    create_contact_details_page,
    edit_passenger_details_page,
    edit_contact_details_page,
    edit_password_page,
    bookings_page,
    login_success
)


class TestUrls(SimpleTestCase):

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_page)

    def test_signup_url_resolves(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup_page)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile_page)

    def test_create_passenger_url_resolves(self):
        url = reverse('create_passenger_details')
        self.assertEquals(resolve(url).func, create_passenger_details_page)

    def test_create_contact_url_resolves(self):
        url = reverse('create_contact_details')
        self.assertEquals(resolve(url).func, create_contact_details_page)

    def test_edit_passenger_url_resolves(self):
        url = reverse('edit_passenger_details')
        self.assertEquals(resolve(url).func, edit_passenger_details_page)

    def test_edit_contact_url_resolves(self):
        url = reverse('edit_contact_details')
        self.assertEquals(resolve(url).func, edit_contact_details_page)

    def test_edit_password_url_resolves(self):
        url = reverse('edit_password')
        self.assertEquals(resolve(url).func, edit_password_page)

    def test_bookings_url_resolves(self):
        url = reverse('bookings')
        self.assertEquals(resolve(url).func, bookings_page)

    def test_login_success_url_resolves(self):
        url = reverse('login_success')
        self.assertEquals(resolve(url).func, login_success)
