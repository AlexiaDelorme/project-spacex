from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from .models import ContactDetail, Passenger
from checkout.models import BookingReference
from .forms import (
    UserSignupForm,
    UserContactDetailForm,
    UserUpdateForm,
    UserPassengerForm
)
from django.contrib.auth.forms import PasswordChangeForm
from datetime import date


@login_required
def logout_page(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('login'))


def signup_page(request):
    """Render sign up form page and provide user feedback if needed."""

    if request.user.is_authenticated:
        return redirect(reverse('login_success'))

    if request.method == "POST":
        signup_form = UserSignupForm(request.POST)

        if signup_form.is_valid():
            signup_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Your account has been created")

                return redirect(reverse('login_success'))
            else:
                messages.warning(
                    request, "We were unable to register your account")
        else:
            messages.warning(request, "Please correct the error(s) below")

    else:
        signup_form = UserSignupForm()

    context = {
        "page_title": "Sign Up",
        "form": signup_form
    }
    return render(request, 'signup.html', context)


@login_required
def profile_page(request):
    """Render user profile page with their personal information:
    contact details, passenger information (if provided yet)"""

    user = User.objects.get(email=request.user.email)

    # Check if user has already provided contact details
    try:
        contact = ContactDetail.objects.get(user=request.user)
    except ContactDetail.DoesNotExist:
        contact = None

    # Check if user has already provided passenger info
    try:
        passenger = Passenger.objects.get(user=request.user)
    except Passenger.DoesNotExist:
        passenger = None

    if contact is not None:
        # User has provided both contact and passenger info
        if passenger is not None:
            context = {
                "page_title": "Profile",
                "user": user,
                "contact": contact,
                "passenger": passenger
            }
        # User has only provided contact details
        else:
            context = {
                "page_title": "Profile",
                "user": user,
                "contact": contact
            }
    else:
        # User has only provided passenger info
        if passenger is not None:
            context = {
                "page_title": "Profile",
                "user": user,
                "passenger": passenger
            }
        # User has not provided neither contact nor passenger info
        else:
            context = {
                "page_title": "Profile",
                "user": user
            }

    return render(request, 'profile/profile.html', context)


@login_required
def create_passenger_details_page(request):
    """Render form to register passenger info"""

    if request.method == 'POST':
        form = UserPassengerForm(request.POST)
        if form.is_valid():
            passenger_details = form.save(commit=False)
            passenger_details.user = request.user
            passenger_details.save()
            messages.success(
                request, "Your passenger details have been saved")
            return redirect('profile')
        else:
            messages.warning(request, "Please correct the error(s) below")
    else:
        form = UserPassengerForm()

    context = {
        "page_title": "Passenger details",
        "form": form
    }

    return render(request, 'profile/create_passenger_details.html', context)


@login_required
def create_contact_details_page(request):
    """Render form to register contact details"""

    if request.method == 'POST':
        form = UserContactDetailForm(request.POST)
        if form.is_valid():
            contact_details = form.save(commit=False)
            contact_details.user = request.user
            contact_details.save()
            messages.success(
                request, "Your contact details have been saved")
            return redirect('profile')
        else:
            messages.warning(request, "Please correct the error(s) below")
    else:
        form = UserContactDetailForm()

    context = {
        "page_title": "Contact details",
        "form": form
    }

    return render(request, 'profile/create_contact_details.html', context)


@login_required
def edit_passenger_details_page(request):
    """Render form to edit passenger info"""

    if request.method == 'POST':
        form = UserPassengerForm(request.POST, instance=request.user.passenger)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your passenger details have been updated")
            return redirect('profile')
        else:
            messages.warning(request, "Please correct the error(s) below")
    else:
        form = UserPassengerForm(instance=request.user.passenger)

    context = {
        "page_title": "Edit passenger",
        "page_name": "edit passenger",
        "form": form
    }

    return render(request, 'profile/edit_passenger_details.html', context)


@login_required
def edit_contact_details_page(request):
    """Render form to edit contact details (including email)"""

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        c_form = UserContactDetailForm(
            request.POST,
            request.FILES,
            instance=request.user.contactdetail)
        if u_form.is_valid() and c_form.is_valid():
            u_form.save()
            c_form.save()
            messages.success(
                request, "Your contact details have been updated")
            return redirect('profile')
        else:
            messages.warning(request, "Please correct the error(s) below")
    else:
        u_form = UserUpdateForm(instance=request.user)
        c_form = UserContactDetailForm(instance=request.user.contactdetail)

    context = {
        "page_title": "Edit contact",
        "u_form": u_form,
        "c_form": c_form
    }

    return render(request, 'profile/edit_contact_details.html', context)


def edit_password_page(request):
    """Render form to edit user's password"""

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, "Your password has been updated")
            return redirect('profile')
        else:
            messages.warning(request, "Please correct the error(s) below")
    else:
        form = PasswordChangeForm(request.user)

    context = {
        "page_title": "Edit password",
        "form": form
    }

    return render(request, 'profile/edit_password.html', context)


@login_required
def bookings_page(request):
    """Render list of upcoming and past trips booked by the user"""

    today = date.today()

    upcoming_bookings = BookingReference.objects.all().filter(
        booker=request.user,
        confirmation_status=True,
        trip__departure_date__gte=today)

    past_bookings = BookingReference.objects.all().filter(
        booker=request.user,
        confirmation_status=True,
        trip__departure_date__lt=today)

    context = {
        "page_title": "Bookings",
        "upcoming_bookings": upcoming_bookings,
        "past_bookings": past_bookings
    }

    return render(request, 'profile/bookings.html', context)


def login_success(request):
    """
    Redirects users based on whether they are about to checkout
    """
    if 'referrer' in request.session:
        del request.session['referrer']
        return redirect(reverse('checkout_contact'))
    else:
        return redirect(reverse('profile'))
