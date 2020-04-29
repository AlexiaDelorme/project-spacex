from django.urls import path
from .views import checkout_passengers_page


urlpatterns = [
    path(
        'passengers/',
        checkout_passengers_page,
        name='checkout_passengers'
    ),
]
