from django.db import models
from django_countries.fields import CountryField
from datetime import timedelta


class DepartureSite(models.Model):
    site_name = models.CharField(max_length=100)
    country = CountryField()
    site_code = models.CharField(max_length=30)

    class Meta:
        ordering = ['country']

    def __str__(self):
        return f"{self.site_name}, {self.country.name}"


class RequiredDocument(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TripImage(models.Model):
    img_name = models.CharField(max_length=50)
    img_file = models.ImageField(blank=True, upload_to='trip_pics')

    class Meta:
        ordering = ['img_name']

    def __str__(self):
        return self.img_name


class TripCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Trip Categories'

    title = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    destination_code = models.CharField(max_length=30)
    duration = models.IntegerField()
    distance = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    required_document = models.ManyToManyField(RequiredDocument)
    img = models.ManyToManyField(TripImage)

    def __str__(self):
        return self.destination


class Trip(models.Model):
    category = models.ForeignKey(TripCategory, on_delete=models.CASCADE)
    departure_site = models.ForeignKey(DepartureSite, on_delete=models.CASCADE)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    return_time = models.TimeField()
    slot = models.IntegerField()

    @property
    def return_date(self):
        return self.departure_date + timedelta(days=self.category.duration)

    def trip_reference(self):
        return f"SPX{self.id}"

    def __str__(self):
        return f"{self.category} - {self.departure_site} - {self.departure_date}"
