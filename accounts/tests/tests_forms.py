from django.test import SimpleTestCase
from accounts.forms import (
    UserUpdateForm,
    UserPassengerForm,
    UserContactDetailForm
)


class TestUserUpdateForm(SimpleTestCase):

    def test_form_is_valid(self):
        form = UserUpdateForm({'email': 'test1@test.com'})

        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        form = UserUpdateForm({'email': ''})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_correct_message_for_missing_field(self):
        form = UserUpdateForm({'email': ''})

        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = UserUpdateForm()

        self.assertEqual(form.Meta.fields, ['email'])


class TestUserPassengerForm(SimpleTestCase):

    def test_form_is_invalid(self):
        form = UserPassengerForm({'title': ''})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    def test_correct_message_for_missing_field(self):
        form = UserPassengerForm({'title': ''})

        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = UserPassengerForm()

        self.assertEqual(form.Meta.fields, [
            'title', 'birth_month', 'birth_day',
            'birth_year', 'citizenship', 'passport_id',
        ])


class TestUserContactDetailForm(SimpleTestCase):

    def test_form_is_invalid(self):
        form = UserContactDetailForm({'country': ''})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

    def test_correct_message_for_missing_field(self):
        form = UserContactDetailForm({'country': ''})

        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = UserContactDetailForm()

        self.assertEqual(form.Meta.fields, [
            'phone_number', 'street_address1', 'street_address2',
            'state', 'postcode', 'town_or_city', 'country'
        ])
