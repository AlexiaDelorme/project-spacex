from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class OtherPassenger(models.Model):

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

    title = models.CharField(max_length=10, choices=CHOICES_TITLE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_month = models.CharField(max_length=20, choices=CHOICES_MONTH)
    birth_day = models.IntegerField()
    birth_year = models.IntegerField()
    citizenship = CountryField()
    passport_id = models.CharField(max_length=30)

    @property
    def birth_date(self):
        return f"{self.birth_month} {self.birth_day}, {self.birth_year}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"