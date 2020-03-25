# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Trip, RequiredDocument, DepartureSite, TripImage, Departure

# Register your models here.
admin.site.register(Trip)

admin.site.register(Departure)

admin.site.register(DepartureSite)

admin.site.register(RequiredDocument)

admin.site.register(TripImage)