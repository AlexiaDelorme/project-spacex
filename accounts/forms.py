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

class UserContactDetailForm(forms.ModelForm):
    class Meta:
        model = ContactDetail
        fields = [
            'phone_number',
            'birth_date',
            'street_address1',
            'street_address2',
            'state',
            'postcode',
            'town_or_city',
            'country',
            'profile_pic'
            ]
