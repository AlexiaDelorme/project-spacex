from django.urls import path
from .views import faq_page

urlpatterns = [
    path('faq/', faq_page, name='faq'),
]
