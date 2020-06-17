"""
URL configuration for home app
"""
from django.urls import path

from home.views import HomeView

app_name = 'cart'
urlpatterns = [
    path('cart', HomeView.as_view(), name="home"),
]