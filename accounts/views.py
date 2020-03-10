from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserSignupForm


@login_required
def logout_page(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return render(request, "logout.html", {"page_title": "Log Out"})


def login_page(request):

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(email=request.POST['email'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('profile'))
            else:
                login_form.add_error(
                    None, "Your email or password is incorrect")

    else:
        login_form = UserLoginForm()
    context = {
        "page_title": "Log In",
        "form": login_form
    }
    return render(request, "login.html", context)


def signup_page(request):
    signup_form = UserSignupForm()
    context = {
        "page_title": "Sign Up",
        "form": signup_form
    }
    return render(request, 'signup.html', context)


def profile_page(request):
    return render(request, 'profile.html', {"page_title": "Profile"})
