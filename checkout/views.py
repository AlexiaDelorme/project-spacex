from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from accounts.models import ContactDetail
from accounts.forms import UserContactDetailForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def checkout_confirm_page(request):
    """Render page to provide passengers details"""

    user = User.objects.get(email=request.user.email)

    try:
        contact = ContactDetail.objects.get(user=request.user)
    except ContactDetail.DoesNotExist:
        contact = None

    if contact is not None:
        form = UserContactDetailForm(instance=request.user.contactdetail)
    else:
        form = UserContactDetailForm()

    context = {
        "page_title": "Booker details",
        "user": user,
        "form": form
    }

    return render(request, "checkout_confirm.html", context)
