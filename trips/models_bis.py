# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.db import models
from django.conf import settings


class DepartureSite(models.Model):
    site_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    class Meta:
        ordering = ['country']

    def __str__(self):
        return f"{self.site_name}, {self.country}"


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


class Trip(models.Model):
    title = models.CharField(max_length=50)
    destination = models.CharField(max_length=30)
    duration = models.IntegerField()
    price = models.IntegerField()
    departure_site = models.ForeignKey(DepartureSite, on_delete=models.CASCADE)
    departure_date = models.DateField()
    return_date = models.DateField()
    slot = models.IntegerField()
    description = models.TextField()
    distance = models.IntegerField()
    required_document = models.ManyToManyField(RequiredDocument)
    img = models.ManyToManyField(TripImage)

    def __str__(self):
        return self.title
