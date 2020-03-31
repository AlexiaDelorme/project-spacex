from django.urls import path
from .views import edit_contact_details_page, create_contact_details_page


urlpatterns = [
    path(
        'create/',
        create_contact_details_page,
        name='create_contact_details'),
    path(
        'edit/',
        edit_contact_details_page,
        name='edit_contact_details'),
]
