# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.forms.models import model_to_dict
from .models import Trip, TripCategory, DepartureSite
import json


def faq_page(request):
    return render(request, "faq.html", {"page_title": "FAQs"})


def trips_page(request):
    trip_categories = TripCategory.objects.all()
    context = {
        "page_title": "All Trips",
        "page_name": "all trips",
        "trip_categories": trip_categories
    }
    return render(request, "trips.html", context)


def trip_detail_page(request, pk):
    trip_category = get_object_or_404(TripCategory, pk=pk)
    trips = Trip.objects.all().filter(category=trip_category)
    departure_sites = DepartureSite.objects.all()
    context = {
        "page_title": "Detail",
        "page_name": "trip details",
        "trip_category": trip_category,
        "trips": trips,
        "departure_sites": departure_sites
    }
    return render(request, "trip_detail.html", context)
