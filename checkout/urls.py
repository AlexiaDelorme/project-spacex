from django.urls import path
from .views import checkout_confirm_page, checkout_passengers_page


urlpatterns = [
    path(
        'confirm/',
        checkout_confirm_page,
        name='checkout_confirm'
    ),
    path(
        'passengers/',
        checkout_passengers_page,
        name='checkout_passengers'
    ),
]
