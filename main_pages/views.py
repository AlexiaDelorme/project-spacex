from django.shortcuts import render, redirect
from django.http import HttpResponseServerError
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages


def home_page(request):
    return render(request, "home.html")


def about_page(request):
    """Render relevant information about the company."""

    return render(request, "about.html", {"page_title": "About Us"})


def contact_page(request):
    """Render contact form for user to get in touch with the company.
    Provide information on the location of the company."""

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(
                request, "Thanks, your request was sent to SpaceX"
            )
            return redirect('contact')
        else:
            messages.warning(
                request, "Sorry, we were enable to send your request"
            )

    else:
        form = ContactForm()

    emailjs_user = settings.EMAILJS_USER
    google_api_key = settings.GOOGLE_API_KEY
    context = {
        "page_title": "Contact Us",
        "form": form,
        "emailjs_user": emailjs_user,
        "google_api_key": google_api_key
    }
    return render(request, "contact.html", context)


def scientists_page(request):
    """Render information regarding scientific research trips"""

    context = {
        "page_title": "Scientific services"
    }
    return render(request, "scientists.html", context)


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


"""
# To be used only to recreate a 500 error
def my_test_500_view(request):
    # Return an "Internal Server Error" 500 response code.
    return HttpResponseServerError
"""
