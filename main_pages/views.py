from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages


def home_page(request):
    return render(request, "home.html")


def about_page(request):
    return render(request, "about.html")


def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(
                request, f'Thank your request was sent!'
            )
            return redirect('contact')
        else:
            messages.error(
                request, f'Sorry, we were enable to send your request!'
            )
        
    else:
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
