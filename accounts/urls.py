from django.urls import path
from .views import logout_page, login_page, signup_page

urlpatterns = [
    path('logout/', logout_page, name='logout'),
    path('login/', login_page, name='login'),
    path('signup/', signup_page, name='signup'),
]
