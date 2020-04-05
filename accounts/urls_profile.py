from django.urls import path
from .views import (
    create_passenger_details_page,
    create_contact_details_page,
    edit_contact_details_page
)


urlpatterns = [
    path(
        'create/passenger/',
        create_passenger_details_page,
        name='create_passenger_details'),
    path(
        'create/contact/',
        create_contact_details_page,
        name='create_contact_details'),
    path(
        'edit/contact/',
        edit_contact_details_page,
        name='edit_contact_details'),
]