from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm

# Create your views here.


def home_page(request):
    return render(request, "home.html")


def about_page(request):
    return render(request, "about.html")


def contact_page(request):
    form = ContactForm()
    emailjs_user = settings.EMAILJS_USER
    context = {
        "form": form,
        "emailjs_user": emailjs_user
    }
    return render(request, "contact.html", context)
