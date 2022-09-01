from django.urls import path
from .views import ProductAPI, ProductVersionAPI, SubscriberAPI, WishlistAPI, WishlistDeleteAPIView

urlpatterns = [
    path('wishlist/', WishlistAPI.as_view(), name = "wishlists"),
    path ('wishlist/delete', WishlistDeleteAPIView.as_view(), name='wishlist_delete'),
    path('products/', ProductAPI.as_view(), name = "products"),
    path('product_versions/', ProductVersionAPI.as_view(), name = "product_versions"),
    path('subscribers/', SubscriberAPI.as_view(), name = "subscribers")
]