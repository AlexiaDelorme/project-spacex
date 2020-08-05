from django.db import models
from django.contrib.auth.models import User


class Testimonial(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.TextField()
    trip_date = models.DateField()
    image = models.ImageField(blank=True, upload_to='testimonial_pics')

    class Meta:
        ordering = ['trip_date']

    def __str__(self):
        return f"{self.passenger.first_name} {self.passenger.last_name} - Trip {self.trip_date}"
