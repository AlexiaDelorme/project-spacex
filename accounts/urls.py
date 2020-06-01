from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (
    logout_page,
    signup_page,
    login_success,
    bookings_page
)


urlpatterns = [
    path('logout/', logout_page, name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True),
        name="login"
    ),
    path('login_success/', login_success, name='login_success'),
    path('signup/', signup_page, name='signup'),
    path('profile/', include('accounts.urls_profile')),
    path('bookings/', bookings_page, name='bookings'),
    path('password-reset/', include('accounts.urls_reset'))
]
