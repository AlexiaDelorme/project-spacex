from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
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

        response = self.client.get('/main/contact/')
        contact_form = response.context['form']

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertEqual(type(contact_form), ContactForm)

    def test_get_user_details_for_contact_form(self):

        # create and log the user in
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='john',
            first_name='John',
            last_name='Lennon',
            email='lennon@thebeatles.com',
            password='johnpassword')
        self.client = Client()
        self.client.login(username='john', password='johnpassword')

        # get contact page
        response = self.client.get('/main/contact/')
        contact_form = response.context['form']

        self.assertEquals(contact_form['first'].value(), 'John')
        self.assertEquals(contact_form['last'].value(), 'Lennon')
        self.assertEquals(
            contact_form['email'].value(), 'lennon@thebeatles.com')

    def test_post_contact_page_success(self):

        post_form = {
            'subject': 'Information Request',
            'first': 'Test',
            'last': 'TestLast',
            'email': 'test@test.com',
            'message': 'This is a test message'
        }
        post_response = self.client.post('/main/contact/', post_form)

        self.assertRedirects(post_response, '/main/contact/')

    def test_post_contact_page_failure(self):

        post_form = {
            'subject': 'Information Request',
            'first': '',
        }
        post_response = self.client.post('/main/contact/', post_form)
        messages = list(post_response.context['messages'])

        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Sorry, we were enable to send your request')

    def test_get_scientists_page(self):

        response = self.client.get('/main/scientists/')
        context = response.context['page_title']

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scientists.html')
        self.assertEqual(context, 'Scientific services')

    def test_get_404_page(self):

        response = self.client.get('/404/')

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
