# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core import serializers
from .models import Trip
import json


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


def trip_detail_page(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    slot = trip.slot
    # Create a string dic to be passed to the dom
    departures = serializers.serialize('json', Trip.objects.all())
    context = {
        "page_title": "Detail",
        "trip": trip,
        "slot": range(slot+1),
        "departures": departures
    }
    return render(request, "trip_detail.html", context)
