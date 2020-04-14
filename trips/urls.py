from django.urls import path
from .views import (
    faq_page,
    trips_categories_page,
    trip_detail_page,
    trips_results_page
)

urlpatterns = [
    path('faq/', faq_page, name='faq'),
    path('categories/', trips_categories_page, name='trips_categories'),
    path('detail/<int:pk>/', trip_detail_page, name='trip_detail'),
    path('results/', trips_results_page, name='trips_results'),
]
