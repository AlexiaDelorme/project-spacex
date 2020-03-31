from django.urls import path
from .views import edit_contact_details_page


urlpatterns = [
    path(
        'edit/',
        edit_contact_details_page,
        name='edit_contact_details'),
]
