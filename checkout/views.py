from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def checkout_passengers_page(request):
    """Render page to provide passengers details"""

    return render(request, "checkout_passengers.html")