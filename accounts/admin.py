# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ContactDetail, Passenger

# Register your models here.
admin.site.register(ContactDetail)
admin.site.register(Passenger)