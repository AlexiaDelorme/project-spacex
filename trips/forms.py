from django import forms
from .models import DepartureSite, TripCategory


class AllTripSearchForm(forms.Form):

    destination = forms.ModelChoiceField(
        queryset=TripCategory.objects.all(),
        empty_label="Choose destination"
    )
    departure_site = forms.ModelChoiceField(
        label='<i class="fas fa-space-shuttle"></i> Departure Site',
        queryset=DepartureSite.objects.all(),
        empty_label="Choose site"
    )
    departure_date = forms.DateField(
        label='<i class="fas fa-calendar-day"></i> Departure Date',
        widget=forms.TextInput(
            attrs={
                'id': 'datepicker',
                'class': 'bg-white'
            }
        )
    )

    class Meta:
        fields = [
            'destination',
            'departure_site',
            'departure_date'
        ]


class TripSearchForm(forms.Form):

    departure_site = forms.ModelChoiceField(
        label='<i class="fas fa-space-shuttle"></i> Departure Site',
        queryset=DepartureSite.objects.all(),
        empty_label="Choose site"
    )
    departure_date = forms.DateField(
        label='<i class="fas fa-calendar-day"></i> Departure Date',
        widget=forms.TextInput(
            attrs={
                'id': 'datepicker',
                'class': 'bg-white'
            }
        )
    )

    class Meta:
        fields = ['departure_site', 'departure_date']
