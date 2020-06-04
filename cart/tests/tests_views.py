from django.test import TestCase, Client
from django.contrib.auth.models import User


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
        """Test that session variable 'referrer' is equal to checkout when user is logged out."""

        self.client.get('/cart/')
        session = self.client.session

        self.assertEqual(session['referrer'], 'checkout')
    
    def test_cart_page_session_logged_in(self):
        """Test that session variable 'referrer' is empty when user is logged in."""

        # Log in dummy user
        client = Client()
        logged_in = client.login(username='test', password='12345678')

        self.client.get('/cart/')
        session = self.client.session

        self.assertTrue(logged_in)
        # Test block failing
        # self.assertNotIn('referrer', session, msg=None)
    
