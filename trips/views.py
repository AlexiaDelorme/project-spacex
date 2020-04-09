# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from .models import Trip, TripCategory, DepartureSite
from .forms import TripSearchForm


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

    if request.method == "POST":
        form = TripSearchForm(request.POST)
        if form.is_valid():
            messages.success(
                request, "SUCCESS - Your form was sent to the server")
            return redirect(reverse('all_trips'))

    else:
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
