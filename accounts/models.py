# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactDetail(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=False)
    birth_date = models.DateField()
    street_address1 = models.CharField(max_length=50, blank=False)
    street_address2 = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=40, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Passenger(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    birth_date = models.DateField()
    citizenship = models.CharField(max_length=30, blank=False)
    passport_id = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"