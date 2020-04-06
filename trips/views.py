# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.forms.models import model_to_dict
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
    # trip_dict = serializers.serialize('json', Trip.objects.all())
    # model_obj_dep = trip_dict["departure"]
    # trip_dict = model_to_dict(trip)
    # departures = serializers.serialize('json', model_obj_dep, fields=('site_name', 'date'))
    departures = [
        {'id': '0',
         'site_name': 'Kourou (CSG)',
         'country': 'French Guyana',
         'date': ['15-04-2020', '15-05-2020', '15-06-2020']
         },
        {'id': '1',
         'site_name': 'Cap Canaveral',
         'country': 'United States',
         'date': ['01-05-2020', '01-06-2020', '01-07-2020']
         }
    ]
    string_departures = json.dumps(departures)
    context = {
        "page_title": "Detail",
        "trip": trip,
        "slot": range(slot+1),
        "departures": departures,
        "string_departures": string_departures
    }
    return render(request, "trip_detail.html", context)
