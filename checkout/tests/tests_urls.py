from django.test import SimpleTestCase
from django.urls import reverse, resolve
from checkout.views import (
    checkout_contact_page,
    checkout_passengers_page,
    save_passenger_to_booking,
    save_user_passenger_to_booking,
    checkout_payment_page,
    checkout_confirmation_page
)


class TestUrls(SimpleTestCase):

    def test_checkout_contact_url_resolves(self):
        url = reverse('checkout_contact')
        self.assertEquals(resolve(url).func, checkout_contact_page)

    def test_checkout_passengers_url_resolves(self):
        url = reverse('checkout_passengers')
        self.assertEquals(resolve(url).func, checkout_passengers_page)

    def test_save_passenger_url_resolves(self):
        url = reverse('save_passenger', args=['1'])
        self.assertEquals(resolve(url).func, save_passenger_to_booking)

    def test_save_user_passenger_url_resolves(self):
        url = reverse('save_user_passenger', args=['1'])
        self.assertEquals(resolve(url).func, save_user_passenger_to_booking)

    def test_checkout_payment_url_resolves(self):
        url = reverse('checkout_payment')
        self.assertEquals(resolve(url).func, checkout_payment_page)

    def test_checkout_confirmation_url_resolves(self):
        url = reverse('checkout_confirmation')
        self.assertEquals(resolve(url).func, checkout_confirmation_page)
