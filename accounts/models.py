from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class ContactDetail(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    street_address1 = models.CharField(max_length=50)
    street_address2 = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=40, blank=True, null=True)
    postcode = models.CharField(max_length=20)
    town_or_city = models.CharField(max_length=40)
    country = CountryField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Passenger(models.Model):

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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10, choices=CHOICES_TITLE)
    birth_month = models.CharField(max_length=20, choices=CHOICES_MONTH)
    birth_day = models.IntegerField()
    birth_year = models.IntegerField()
    citizenship = CountryField()
    passport_id = models.CharField(max_length=30)
    confirmation_status = models.BooleanField(default=False)

    @property
    def birth_date(self):
        return f"{self.birth_month} {self.birth_day}, {self.birth_year}"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
