from django import forms
from .models import OtherPassenger
from datetime import date


class OtherPassengerForm(forms.ModelForm):

    CHOICES_TITLE = [
        ('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Ms', 'Ms')
    ]
    CHOICES_MONTH = [('January', 'January'),
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
