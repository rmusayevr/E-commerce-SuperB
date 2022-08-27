from django.urls import path
from .views import AddressInfo, BillingInfo, ShippingInfo, checkout, shopping_cart, wishlist

urlpatterns = [
    path('address_info/', AddressInfo.as_view(), name = "address_info"),
    path('billing_info/', BillingInfo.as_view(), name = "billing_info"),
    path('shipping_info/', ShippingInfo.as_view(), name = "shipping_info"),
    path('checkout/', checkout, name = "checkout"),
    path('shopping_cart/', shopping_cart, name = "shopping_cart"),
    path('wishlist/', wishlist, name = 'wishlist')
]