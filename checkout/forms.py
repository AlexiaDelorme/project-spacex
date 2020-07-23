from django import forms
from .models import OtherPassenger
from datetime import date


class OtherPassengerForm(forms.ModelForm):

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
        model = OtherPassenger
        fields = [
            'title',
            'first_name',
            'last_name',
            'birth_month',
            'birth_day',
            'birth_year',
            'citizenship',
            'passport_id',
        ]


class PaymentForm(forms.Form):

    today = date.today()

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(today.year, 2036)]

    credit_card_number = forms.CharField(
        label='Credit card number',
        max_length=16,
        min_length=16,
        required=False
    )
    cvv = forms.CharField(
        label='Security code (CVV)',
        max_length=3,
        min_length=3,
        required=False
    )
    expiry_month = forms.ChoiceField(
        label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
