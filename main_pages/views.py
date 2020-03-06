from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm


def home_page(request):
    return render(request, "home.html")


def about_page(request):
    return render(request, "about.html")


def contact_page(request):
    form = ContactForm()
    emailjs_user = settings.EMAILJS_USER
    google_api_key = settings.GOOGLE_API_KEY
    context = {
        "page_name": "contact",
        "form": form,
        "emailjs_user": emailjs_user,
        "google_api_key": google_api_key
    }
    return render(request, "contact.html", context)
