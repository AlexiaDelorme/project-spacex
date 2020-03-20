from django import forms


class ContactForm(forms.Form):
    """Contact form for contact page"""
    SUBJECT_CHOICES = (
        ("Information Request", "Information Request"),
        ("Tickets Booking", "Tickets Booking"),
        ("Medical Question", "Medical Question"),
        ("Scientific Trips", "Scientific Trips"),
        ("Other", "Other")
    )

    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES
    )
    first = forms.CharField(label='First name')
    last = forms.CharField(label='Last name')
    email = forms.EmailField(label='Email address')
    message = forms.CharField(
        label='Your message',
        widget=forms.Textarea(
            attrs={
                "rows": 10,
            },
        ),
    )

    class Meta:
        fields = ['subject', 'first', 'last', 'email', 'message']
