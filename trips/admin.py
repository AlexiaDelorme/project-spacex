# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (
    TripCategory,
    DepartureSite,
    TripImage,
    RequiredDocument,
    Trip
)

# Register your models here.
admin.site.register(DepartureSite)

admin.site.register(RequiredDocument)

admin.site.register(TripImage)

admin.site.register(TripCategory)

admin.site.register(Trip)
