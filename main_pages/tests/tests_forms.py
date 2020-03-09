from django.test import TestCase
from main_pages.forms import ContactForm


class TestContactForm(TestCase):

    def test_cannot_send_form_with_just_a_field(self):
        form = ContactForm({'first': 'Test'})
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_field(self):
        form = ContactForm({'first': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first'], [f'This field is required.'])
