from django.shortcuts import render, HttpResponse
from .forms import ContactForm

# Create your views here.


def home_page(request):
    return render(request, "home.html")


def about_page(request):
    return render(request, "about.html")


def contact_page(request):
    form = ContactForm()
    return render(request, "contact.html", {'form': form})
