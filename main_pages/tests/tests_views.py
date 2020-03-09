from django.test import TestCase
from main_pages.forms import ContactForm


class TestMainPageViews(TestCase):
    
    def test_get_home_page(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'home.html')

    def test_get_about_page(self):
        page = self.client.get('/main/about/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'about.html')

    def test_get_contact_page(self):
        page = self.client.get('/main/contact/')
        contact_form = page.context['form']
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'contact.html')
        self.assertEqual(type(contact_form), ContactForm)
