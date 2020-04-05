from django.urls import path, include
from .views import (
    logout_page,
    login_page,
    signup_page
)


urlpatterns = [
    path('logout/', logout_page, name='logout'),
    path('login/', login_page, name='login'),
    path('signup/', signup_page, name='signup'),
    path('profile/', include('accounts.urls_profile')),
    path('password-reset/', include('accounts.urls_reset'))
]
