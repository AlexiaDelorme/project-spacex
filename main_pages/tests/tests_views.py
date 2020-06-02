from django.test import TestCase
from main_pages.forms import ContactForm


class TestMainPageViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_get_about_page(self):
        response = self.client.get('/main/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_get_contact_page(self):
        # Testing get request
        response = self.client.get('/main/contact/')
        contact_form = response.context['form']
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertEqual(type(contact_form), ContactForm)
        # Testing post request
        post_form = {
            'subject': 'Information Request',
            'first': 'Test',
            'last': 'TestLast',
            'email': 'test@test.com',
            'message': 'This is a test message'
        }
        post_response = self.client.post('/main/contact/', post_form)
        self.assertRedirects(post_response, '/main/contact/')

    def test_get_scientists_page(self):
        response = self.client.get('/main/scientists/')
        context = response.context['page_title']
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scientists.html')
        self.assertEqual(context, 'Scientific services')
