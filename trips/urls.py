from django.urls import path
from .views import faq_page, trips_page, trip_detail_page

urlpatterns = [
    path('faq/', faq_page, name='faq'),
    path('all-trips/', trips_page, name='all_trips'),
    path('trip-detail/<int:pk>/', trip_detail_page, name='trip_detail'),
]
