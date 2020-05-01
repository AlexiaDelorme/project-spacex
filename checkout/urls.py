from django.urls import path
from .views import checkout_confirm_page


urlpatterns = [
    path(
        'confirm/',
        checkout_confirm_page,
        name='checkout_confirm'
    ),
]
