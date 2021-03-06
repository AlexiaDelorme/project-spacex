from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date
from .models import Trip, TripCategory
from .forms import TripSearchForm, AllTripSearchForm


def faq_page(request):
    return render(request, "faq.html", {"page_title": "FAQs"})


def trips_destinations_page(request):
    """Render page to browse trips by categories/types of destination"""

    trip_categories = TripCategory.objects.all()
    context = {
        "page_title": "Trips destinations",
        "trip_categories": trip_categories
    }
    return render(request, "trips_destinations.html", context)


def trip_detail_page(request, pk):
    """View trip detail about a specific trip category/destination"""

    form = TripSearchForm()

    # Return all the trips matching the trip category id
    trip_category = get_object_or_404(TripCategory, pk=pk)
    trips = Trip.objects.all().filter(category=trip_category)

    context = {
        "page_title": "Detail",
        "trip_category": trip_category,
        "trips": trips,
        "form": form
    }
    return render(request, "trip_detail.html", context)


def trips_results_page(request, pk):
    """Display trips matching the criteria provided in the form"""

    # Load fields provided in the form
    form = request.POST
    departure_site = form.get('departure_site')
    departure_date = form.get('departure_date')

    # Return all trips matching the criteria provided in the form
    trip_category = get_object_or_404(TripCategory, pk=pk)
    trips = Trip.objects.all().filter(
        category=trip_category,
        departure_site=departure_site,
        departure_date__gte=(departure_date)
    )
    trip_result = len(trips)

    # Set pagination for trips results
    paginator = Paginator(trips, 5)  # Show 5 trips per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_title": "Results",
        "trip_result": trip_result,
        "page_obj": page_obj,
        "trip_category": trip_category
    }
    messages.info(
        request, f"Please, see below the result(s) for your search. This includes trips departing on {departure_date} or later.")
    return render(request, "trips_results.html", context)


def trips_all_page(request):
    """Display all the trips available for booking or matching search form."""

    trip_categories = TripCategory.objects.all()

    if request.method == "POST":

        # Set fields provided in the form as variable for query
        form = AllTripSearchForm(request.POST)
        category_id = int(request.POST['destination'])
        departure_site = request.POST['departure_site']
        departure_date = request.POST['departure_date']

        # Return all trips matching the criteria provided in the form
        trip_category = get_object_or_404(TripCategory, pk=category_id)
        trips = Trip.objects.all().filter(
            category=trip_category,
            departure_site=departure_site,
            departure_date__gte=(departure_date)
        )

        # Set pagination for trips results
        paginator = Paginator(trips, 5)  # Show 5 trips per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        messages.info(
            request, f"Please, see below the result(s) for your search. This includes trips departing on {departure_date} or later.")

    else:
        today = date.today()
        trips = Trip.objects.all().filter(departure_date__gte=(today))

        # Set pagination for trips results
        paginator = Paginator(trips, 5)  # Show 5 trips per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        form = AllTripSearchForm()

    trip_result = len(trips)
    context = {
        "page_title": "Search all",
        "trip_result": trip_result,
        "page_obj": page_obj,
        "trip_categories": trip_categories,
        "form": form
    }

    return render(request, "trips_all.html", context)
