# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Date, Departure, TripImage, RequiredDocument, Trip

# Register your models here.
admin.site.register(Date)

admin.site.register(Departure)

admin.site.register(TripImage)

admin.site.register(RequiredDocument)

admin.site.register(Trip)
