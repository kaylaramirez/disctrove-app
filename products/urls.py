"""
URL configuration for inventory app
"""
from django.urls import path, include
from products.views import ProductView, ManufacturerView, DetailsView


app_name = 'products'
urlpatterns = [
    # path('', include(router.urls)),
    path('<str:manufacturer>/<str:disc>/', DetailsView.as_view(), name='disc-details'),
    path('<str:manufacturer>/', ManufacturerView.as_view(), name="manufacturer"),
    path('', ProductView.as_view(), name='product'),
]
