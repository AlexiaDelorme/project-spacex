from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from accounts.models import Passenger
from accounts.forms import UserPassengerForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def checkout_passengers_page(request):
    """Render page to provide passengers details"""

    user = User.objects.get(email=request.user.email)

    try:
        passenger = Passenger.objects.get(user=request.user)
    except Passenger.DoesNotExist:
        passenger = None

    if passenger is not None:
        form = UserPassengerForm(instance=request.user.passenger)
    else:
        form = UserPassengerForm()

    context = {
        "page_title": "Passenger details",
        "user": user,
        "form": form
    }

    return render(request, "checkout_passengers.html", context)
