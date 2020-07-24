from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib.auth.models import User
from accounts.models import ContactDetail, Passenger
from .models import BookingReference
from trips.models import Trip
from accounts.forms import UserContactDetailForm, UserPassengerForm
from .forms import OtherPassengerForm, PaymentForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
import stripe


@login_required(redirect_field_name='next')
def checkout_contact_page(request):
    """Render page to confirm checkout and booker's contact details"""

    # Redirect users to cart if they try to access this page with an empty cart
    if not request.session.get('cart'):
        return redirect('view_cart')

    user = User.objects.get(email=request.user.email)

    # Clear existing booking references
    # (if user has clicked prev btn on passenger page)
    if 'booking_references' in request.session:
        booking_references = request.session['booking_references']
        for key in booking_references:
            BookingReference.objects.filter(
                id=booking_references[key]).delete()
        del request.session['booking_references']

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
                messages.success(
                    request, "Your contact details have been saved")
                return redirect(reverse('checkout_passengers'))
            else:
                messages.warning(request, "Please correct the error(s) below")
        else:
            form = UserContactDetailForm(instance=request.user.contactdetail)

    # Create new instance of ContactDetail model
    else:
        if request.method == 'POST':
            form = UserContactDetailForm(request.POST)
            if form.is_valid():
                # Save new contact details
                contact_details = form.save(commit=False)
                contact_details.user = request.user
                contact_details.save()
                messages.success(
                    request, "Your contact details have been saved")
                return redirect(reverse('checkout_passengers'))
            else:
                messages.warning(request, "Please correct the error(s) below")
        else:
            form = UserContactDetailForm()

    context = {
        "page_title": "Contact details",
        "checkout_pg": "contact",
        "user": user,
        "form": form
    }

    return render(request, "checkout_contact.html", context)


@login_required
def checkout_passengers_page(request):
    """Create booking reference for each trip in cart. Render page to provide
    passengers details"""

    # Redirect users to cart if they try to access this page with an empty cart
    if not request.session.get('cart'):
        return redirect('view_cart')

    user = User.objects.get(email=request.user.email)

    # Create booking reference for trips
    if 'booking_references' not in request.session:
        cart = request.session.get('cart', {})
        ref = {}
        for id in cart:
            # Create booking ref object
            booking_obj = BookingReference.objects.create(
                booker=user,
                trip=Trip.objects.get(id=id),
                passenger_number=cart[id]
            )
            booking_id = booking_obj.id
            # Store this booking id as value in ref dictionary
            ref[id] = ref.get(id, booking_id)
        request.session['booking_references'] = ref

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
        "checkout_pg": "passengers",
        "user": user,
        "form": form,
        "o_form": o_form
    }

    return render(request, "checkout_passengers.html", context)


@login_required
def save_passenger_to_booking(request, id):
    """Temporarily save passenger as object in the db. Then, assign their id
    to the corresponding booking reference. The id corresponds to the trip that
    the passenger will be registered to."""

    passenger_form = OtherPassengerForm(request.POST)
    registered_passenger = passenger_form.save()

    # Add this passenger to the corresponding booking reference
    booking_references = request.session.get('booking_references', {})
    booking_id = booking_references[str(id)]
    booking_obj = get_object_or_404(BookingReference, id=booking_id)
    booking_obj.other_passenger.add(
        registered_passenger
    )

    messages.success(request, "Passenger details have been saved")
    return redirect(reverse('checkout_passengers'))


@login_required
def save_user_passenger_to_booking(request, id):
    """Save passenger details for autehnticated user. Then, assign their id
    to the corresponding booking reference. The id corresponds to the trip
    that the passenger will be registered to."""

    # Check if user already provided passenger details
    try:
        passenger = Passenger.objects.get(user=request.user)
    except Passenger.DoesNotExist:
        passenger = None

    # Save existing passenger details for this user
    if passenger is not None:
        user_passenger_form = UserPassengerForm(
            request.POST,
            instance=request.user.passenger
        )
        registered_passenger = user_passenger_form.save()

    # Create new instance of passenger model for this user
    else:
        user_passenger_form = UserPassengerForm(request.POST)
        registered_passenger = user_passenger_form.save(commit=False)
        registered_passenger.user = request.user
        registered_passenger.save()

    # Add this passenger to the corresponding booking reference
    booking_references = request.session.get('booking_references', {})
    booking_id = booking_references[str(id)]
    booking_obj = get_object_or_404(BookingReference, id=booking_id)
    booking_obj.user_passenger = registered_passenger
    booking_obj.save()

    messages.success(request, "Passenger details have been saved")
    return redirect(reverse('checkout_passengers'))


stripe.api_key = settings.STRIPE_SECRET


@login_required
def checkout_payment_page(request):

    # Redirect users to cart if they try to access this page with an empty cart
    if not request.session.get('cart'):
        return redirect('view_cart')

    if request.method == "POST":

        payment_form = PaymentForm(request.POST)

        if payment_form.is_valid():
            cart = request.session.get('cart', {})
            total = 0
            for id, passenger in cart.items():
                trip = get_object_or_404(Trip, pk=id)
                total = passenger * trip.category.price

            # Make stripe payment
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
                if customer.paid:
                    # Set booking references to status confirmed
                    booking_references = request.session.get(
                        'booking_references', {})
                    for key in booking_references:
                        booking_obj = get_object_or_404(
                            BookingReference,
                            id=booking_references[key]
                        )
                        booking_obj.confirmation_status = True
                        booking_obj.order_date = datetime.now()
                        booking_obj.save()
                    # Decrement trip slots by number of passengers booked
                    for id, passenger in cart.items():
                        booked_trip = get_object_or_404(Trip, pk=id)
                        booked_trip.slot -= passenger
                        booked_trip.save()

                    # Empty cart
                    request.session['cart'] = {}

                    messages.success(
                        request,
                        "Your payment was accepted and your booking is confirmed"
                    )
                    return redirect(reverse('checkout_confirmation'))
                else:
                    messages.warning(
                        request, "Sorry, we were unable to take payment")

            except stripe.error.CardError:
                messages.warning(request, "Your card was declined")

        else:
            messages.warning(
                request, "We were unable to take a payment with that card")

    else:
        payment_form = PaymentForm()

    context = {
        "page_title": "Payment",
        "checkout_pg": "payment",
        "form": payment_form,
        "publishable": settings.STRIPE_PUBLISHABLE
    }

    return render(request, "checkout_payment.html", context)


@login_required
def checkout_confirmation_page(request):

    # Create a bookings var for context
    booking_references = request.session.get('booking_references', {})
    bookings = []
    for key in booking_references:
        booking_obj = get_object_or_404(
            BookingReference,
            id=booking_references[key]
        )
        bookings.append(booking_obj)

    # Delete session variable
    if 'booking_references' in request.session:
        del request.session['booking_references']

    context = {
        "page_title": "Confirmation",
        "checkout_pg": "confirmation",
        "bookings": bookings,
        "user": request.user,
    }

    # Send a confirmation email to the user
    subject = "[SpaceX] Your booking is confirmed"
    rendered_message = render_to_string('email.html', context)
    recepient = request.user.email
    send_mail(subject, rendered_message,
              settings.EMAIL_HOST_USER,
              [recepient], fail_silently=False,
              html_message=rendered_message)

    return render(request, "checkout_confirmation.html", context)
