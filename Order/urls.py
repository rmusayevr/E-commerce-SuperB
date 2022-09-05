from django.urls import path

from Order.models import Wishlist
from .views import AddressInfo, BillingInfo, ShippingInfo, checkout, BasketView, WishlistView

urlpatterns = [
    path('address_info/', AddressInfo.as_view(), name = "address_info"),
    path('billing_info/', BillingInfo.as_view(), name = "billing_info"),
    path('shipping_info/', ShippingInfo.as_view(), name = "shipping_info"),
    path('checkout/', checkout, name = "checkout"),
    path('shopping_cart/', BasketView.as_view(), name = "shopping_cart"),
    path('wishlist/', WishlistView.as_view(), name = 'wishlist')
]