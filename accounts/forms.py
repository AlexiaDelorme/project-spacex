from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import ContactDetail, Passenger


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserSignupForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']

class UserContactDetailForm(forms.ModelForm):
    class Meta:
        model = ContactDetail
        fields = [
            'birth_date',
            'citizenship',
            'passport_id',
            'phone_number',
            'street_address1',
            'street_address2',
            'state',
            'postcode',
            'town_or_city',
            'country'
            ]


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'citizenship',
            'passport_id'
            ]
