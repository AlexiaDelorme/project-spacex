from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import ContactDetail, Passenger
from .models import OtherPassenger, BookingReference
from trips.models import Trip
from accounts.forms import UserContactDetailForm, UserPassengerForm
from .forms import OtherPassengerForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages

# Create your views here.


@login_required
def checkout_confirm_page(request):
    """Render page to confirm checkcout and booker's contact details"""

    user = User.objects.get(email=request.user.email)

    # Check if user already provided contact details
    try:
        contact = ContactDetail.objects.get(user=request.user)
    except ContactDetail.DoesNotExist:
        contact = None

    # Load contact form with pre-filled fields
    if contact is not None:
        if request.method == 'POST':
            form = UserContactDetailForm(
                request.POST,
                request.FILES,
                instance=request.user.contactdetail)
            if form.is_valid():
                form.save()

                # ----- Code under test
                # Create booking reference for trips in cart

                cart = request.session.get('cart', {})
                ref = {}

                for id in cart:
                    print(f"The trip id is {id}")
                    # Create booking ref object
                    booking_obj = BookingReference.objects.create(
                        booker=User.objects.get(id=request.user.id),
                        trip=Trip.objects.get(id=id)
                    )
                    # Get id of this booking ref object
                    booking_id = booking_obj.id
                    print(f"The booking id is {booking_id}")
                    # Store this booking id as value in ref dictionary
                    ref[id] = ref.get(id, booking_id)

                request.session['booking_references'] = ref
                print(ref)
                # ----- End of code under test

                messages.success(
                    request, f'Your contact details have been saved!')
                return redirect(reverse('checkout_passengers'))
        else:
            form = UserContactDetailForm(instance=request.user.contactdetail)

    # Create new instance of ContactDetail model
    else:
        if request.method == 'POST':
            form = UserContactDetailForm(request.POST)
            if form.is_valid():
                contact_details = form.save(commit=False)
                contact_details.user = request.user
                contact_details.save()
                messages.success(
                    request, f'Your contact details have been saved!')
                return redirect(reverse('checkout_passengers'))
        else:
            form = UserContactDetailForm()

    context = {
        "page_title": "Booker details",
        "user": user,
        "form": form
    }

    return render(request, "checkout_confirm.html", context)


@login_required
def checkout_passengers_page(request):
    """Render page to provide passengers details"""

    user = User.objects.get(email=request.user.email)

    # Check if user already provided passenger details
    try:
        passenger = Passenger.objects.get(user=request.user)
    except Passenger.DoesNotExist:
        passenger = None

    if passenger is not None:
        form = UserPassengerForm(instance=request.user.passenger)
    else:
        form = UserPassengerForm()

    o_form = OtherPassengerForm()
    context = {
        "page_title": "Passenger details",
        "user": user,
        "form": form,
        "o_form": o_form
    }

    return render(request, "checkout_passengers.html", context)


def save_passenger_to_booking(request, id):
    """Temporarily save passenger as object in the db.
    Then assign their id to the corresponding booking reference.
    The id corresponds to the trip that the passenger will be registered to."""

    # Save passenger form
    passenger_form = OtherPassengerForm(request.POST)
    print(request.POST)
    registered_passenger = passenger_form.save()
    # Get the id of this newly created passenger instance
    passenger_id = registered_passenger.id

    # Add this passenger id to the corresponding booking reference
    booking_references = request.session.get('booking_references', {})
    booking_id = booking_references[str(id)]
    booking_obj = get_object_or_404(BookingReference, id=booking_id)
    booking_obj.other_passenger.add(
        OtherPassenger.objects.get(id=passenger_id)
    )

    messages.success(request, "Passenger saved!")
    return redirect(reverse('checkout_passengers'))
