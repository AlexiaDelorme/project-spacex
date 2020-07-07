from django.urls import path
from .views import (
    faq_page,
    trips_destinations_page,
    trip_detail_page,
    trips_results_page,
    trips_all_page
)

urlpatterns = [
    path('faq/', faq_page, name='faq'),
    path('destinations/', trips_destinations_page, name='trips_destinations'),
    path('detail/<int:pk>/', trip_detail_page, name='trip_detail'),
    path('results/<int:pk>/', trips_results_page, name='trips_results'),
    path('all/', trips_all_page, name='trips_all'),
]
