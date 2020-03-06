from django import forms


class ContactForm(forms.Form):
    """Contact for contact page"""

    subject = forms.ChoiceField(
        choices=(("Information Request", "Information Request"), ("Tickets Booking", "Tickets Booking"), ("Medical Question", "Medical Question"))
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
