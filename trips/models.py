# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class DepartureSite(models.Model):
    site = models.CharField(max_length=100)

    def __str__(self):
        return self.site


class RequiredDocument(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Trip(models.Model):
    title = models.CharField(max_length=50)
    destination = models.CharField(max_length=30)
    duration = models.DurationField()
    price = models.IntegerField()
    departure_date = models.DateField()
    departure_site = models.ForeignKey(
        DepartureSite, on_delete=models.PROTECT)
    slot = models.IntegerField()
    description = models.TextField()
    distance = models.IntegerField()
    required_document = models.ForeignKey(
        RequiredDocument, on_delete=models.PROTECT)
    img = models.FileField(blank=True)

    def __str__(self):
        return self.title
