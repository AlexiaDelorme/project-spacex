from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main_pages.views import (
    home_page,
    contact_page,
    about_page,
    scientists_page
)


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home_page)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about_page)

    def test_contact_url_resolves(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact_page)

    def test_scientists_url_resolves(self):
        url = reverse('scientists')
        self.assertEquals(resolve(url).func, scientists_page)
