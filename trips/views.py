# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from .models import Trip, TripCategory, DepartureSite
from .forms import TripSearchForm
from datetime import datetime, date


def faq_page(request):
    return render(request, "faq.html", {"page_title": "FAQs"})


def trips_categories_page(request):
    trip_categories = TripCategory.objects.all()
    context = {
        "page_title": "Trips categories",
        "page_name": "trip categories",
        "trip_categories": trip_categories
    }
    return render(request, "trips_categories.html", context)


def trip_detail_page(request, pk):

    form = TripSearchForm()

    trip_category = get_object_or_404(TripCategory, pk=pk)
    trips = Trip.objects.all().filter(category=trip_category)
    context = {
        "page_title": "Detail",
        "page_name": "trip details",
        "trip_category": trip_category,
        "trips": trips,
        "form": form
    }
    return render(request, "trip_detail.html", context)


def trips_results_page(request, pk):
    form = request.POST
    departure_site = form.get('departure_site')
    departure_date = form.get('departure_date')
    passenger_number = form.get('passenger_number')

    trip_category = get_object_or_404(TripCategory, pk=pk)
    trips = Trip.objects.all().filter(
        category=trip_category,
        departure_site=departure_site,
        departure_date__gte=date(departure_date)
    )

    context = {
        "page_title": "Results",
        "page_name": "results",
        "trips": trips,
    }
    return render(request, "trips_results.html", context)
