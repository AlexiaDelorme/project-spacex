# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Trip


def faq_page(request):
    return render(request, "faq.html", {"page_title": "FAQs"})


def trips_page(request):
    trips = Trip.objects.all()
    context = {
        "page_title": "All Trips",
        "page_name": "all trips",
        "trips": trips
    }
    return render(request, "trips.html", context)
