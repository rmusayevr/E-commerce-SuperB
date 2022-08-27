from django.urls import path
from .views import ProductAPI, ProductVersionAPI

urlpatterns = [
    path('products/', ProductAPI.as_view(), name = "products"),
    path('product_versions/', ProductVersionAPI.as_view(), name = "product_versions"),
]