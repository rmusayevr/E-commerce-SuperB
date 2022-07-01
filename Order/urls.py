from django.urls import path
from .views import checkout_billing_info, checkout, shopping_cart

urlpatterns = [
    path('checkout_billing_info/', checkout_billing_info, name = "checkout_billing_info"),
    path('checkout/', checkout, name = "checkout"),
    path('shopping_cart/', shopping_cart, name = "shopping_cart"),
]