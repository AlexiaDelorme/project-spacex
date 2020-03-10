from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import UserLoginForm


def logout_page(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return render(request, "logout.html")


def login_page(request):
    login_form = UserLoginForm()
    return render(request, "login.html", {'form': login_form})

