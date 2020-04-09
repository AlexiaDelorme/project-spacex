from django import forms
from .models import DepartureSite


class TripSearchForm(forms.Form):

    departure_site = forms.ModelChoiceField(
        queryset=DepartureSite.objects.all(),
        empty_label="Choose site"
    )
    departure_date = forms.DateField()
    passenger_number = forms.IntegerField(max_value=5, min_value=1)

    class Meta:
        fields = ['departure_site', 'departure_date', 'passenger_number']
