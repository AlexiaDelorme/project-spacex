from django.urls import path
from .views import (
    checkout_contact_page,
    checkout_passengers_page,
    save_passenger_to_booking,
    save_user_passenger_to_booking,
    checkout_payment_page)


urlpatterns = [
    path(
        'contact/',
        checkout_contact_page,
        name='checkout_contact'
    ),
    path(
        'passengers/',
        checkout_passengers_page,
        name='checkout_passengers'
    ),
    path(
        'save-passenger/<int:id>/',
        save_passenger_to_booking,
        name='save_passenger'
    ),
    path(
        'save-user-passenger/<int:id>/',
        save_user_passenger_to_booking,
        name='save_user_passenger'
    ),
    path('payment/', checkout_payment_page, name='checkout_payment'),
]
