from django import forms


class TripSearchForm(forms.Form):
    """Trip search form for all trips listing page"""

    DEPARTURE_CHOICES = (
        ("1", "Departure site 1"),
        ("2", "Departure site 2"),
        ("3", "Departure site 3"),
        ("4", "Departure site 4")
    )

    destination = forms.CharField()

    departure_site = forms.ChoiceField(
        choices=DEPARTURE_CHOICES
    )
    departure_date = forms.DateField()

    class Meta:
        fields = ['destination', 'departure_site', 'departure_date']
