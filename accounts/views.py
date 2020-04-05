from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ContactDetail, Passenger
from .forms import (
    UserLoginForm,
    UserSignupForm,
    UserContactDetailForm,
    UserUpdateForm,
    UserPassengerForm
)


@login_required
def logout_page(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('login'))


def login_page(request):

    if request.user.is_authenticated:
        return redirect(reverse('profile'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('profile'))
            else:
                login_form.add_error(
                    None, "Your username or password is incorrect")

    else:
        login_form = UserLoginForm()
    context = {
        "page_title": "Log In",
        "form": login_form
    }
    return render(request, "login.html", context)


def signup_page(request):

    if request.user.is_authenticated:
        return redirect(reverse('profile'))

    if request.method == "POST":
        signup_form = UserSignupForm(request.POST)

        if signup_form.is_valid():
            signup_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Your account has been created")
                return redirect(reverse('profile'))
            else:
                messages.error(
                    request, "We were unable to register your account.")

    else:
        signup_form = UserSignupForm()

    context = {
        "page_title": "Sign Up",
        "form": signup_form
    }
    return render(request, 'signup.html', context)


@login_required
def profile_page(request):

    user = User.objects.get(email=request.user.email)

    try:
        contact = ContactDetail.objects.get(user=request.user)
    except ContactDetail.DoesNotExist:
        contact = None

    try:
        passenger = Passenger.objects.get(user=request.user)
    except Passenger.DoesNotExist:
        passenger = None

    if contact is not None:
        if passenger is not None:
            context = {
                "page_title": "Profile",
                "user": user,
                "contact": contact,
                "passenger": passenger
            }
        else:
            context = {
                "page_title": "Profile",
                "user": user,
                "contact": contact
            }
    else:
        if passenger is not None:
            context = {
                "page_title": "Profile",
                "user": user,
                "passenger": passenger
            }
        else:
            context = {
                "page_title": "Profile",
                "user": user
            }

    return render(request, 'profile.html', context)


@login_required
def create_passenger_details_page(request):

    if request.method == 'POST':
        form = UserPassengerForm(request.POST)
        if form.is_valid():
            passenger_details = form.save(commit=False)
            passenger_details.user = request.user
            passenger_details.first_name = request.user.first_name
            passenger_details.last_name = request.user.last_name
            passenger_details.save()
            messages.success(
                request, f'Your passenger details have been saved!')
            return redirect('profile')
    else:
        form = UserPassengerForm()

    context = {
        "page_title": "Passenger details",
        "form": form
    }

    return render(request, 'profile/create_passenger_details.html', context)


@login_required
def create_contact_details_page(request):

    if request.method == 'POST':
        form = UserContactDetailForm(request.POST)
        if form.is_valid():
            contact_details = form.save(commit=False)
            contact_details.user = request.user
            contact_details.save()
            messages.success(
                request, f'Your contact details have been saved!')
            return redirect('profile')
    else:
        form = UserContactDetailForm()

    context = {
        "page_title": "Contact details",
        "form": form
    }

    return render(request, 'profile/create_contact_details.html', context)


@login_required
def edit_passenger_details_page(request):

    if request.method == 'POST':
        form = UserPassengerForm(request.POST, instance=request.user.passenger)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your passenger details have been updated!')
            return redirect('profile')
    else:
        form = UserPassengerForm(instance=request.user.passenger)

    context = {
        "page_title": "Edit passenger",
        "form": form
    }

    return render(request, 'profile/edit_passenger_details.html', context)


@login_required
def edit_contact_details_page(request):

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
                request, f'Your contact details have been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        c_form = UserContactDetailForm(instance=request.user.contactdetail)

    context = {
        "page_title": "Edit contact",
        "u_form": u_form,
        "c_form": c_form
    }

    return render(request, 'profile/edit_contact_details.html', context)
