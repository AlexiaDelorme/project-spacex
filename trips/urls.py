from django.urls import path
from .views import faq_page, trips_page

urlpatterns = [
    path('faq/', faq_page, name='faq'),
    path('all-trips/', trips_page, name='all-trips'),
]
