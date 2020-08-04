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
        f"{self.passenger} - trip {self.trip_date}"
