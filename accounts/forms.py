from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ContactDetail, Passenger
from datetime import date


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


class UserPassengerForm(forms.ModelForm):

    CHOICES_TITLE = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Ms', 'Ms')
    ]
    CHOICES_MONTH = [
        ("", "---------"),
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    ]

    today = date.today()

    title = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                'class': 'col-3'
            }
        ),
        choices=CHOICES_TITLE
    )
    birth_month = forms.ChoiceField(choices=CHOICES_MONTH)
    birth_year = forms.IntegerField(
        min_value=1910,
        max_value=today.year
    )
    birth_day = forms.IntegerField(
        min_value=1,
        max_value=31
    )

    class Meta:
        model = Passenger
        fields = [
            'title',
            'birth_month',
            'birth_day',
            'birth_year',
            'citizenship',
            'passport_id',
        ]


class UserContactDetailForm(forms.ModelForm):
    class Meta:
        model = ContactDetail
        fields = [
            'phone_number',
            'street_address1',
            'street_address2',
            'state',
            'postcode',
            'town_or_city',
            'country'
        ]
