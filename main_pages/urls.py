from django.urls import path
from .views import about_page, contact_page, scientists_page

urlpatterns = [
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('scientists/', scientists_page, name='scientists'),
]
