from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from Product.models import Product, Product_version
from Core.models import Subscription
from Order.models import Wishlist
from .serializers import (
                    ProductReadSerializer, 
                    ProductVersionSerializer,
                    SubscriberSerializer,
                    WishlistSerializer
                )
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class ProductAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer

class ProductVersionAPI(ListAPIView):
    queryset = Product_version.objects.all()
    serializer_class = ProductVersionSerializer

class SubscriberAPI(ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriberSerializer

class WishlistAPI(APIView):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user.products_wishlist)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')[0]
        product = Product_version.objects.filter(pk=product_id).first()
        if product:
            wishlist, created = Wishlist.objects.get_or_create(user = request.user)
            wishlist2 = Wishlist.objects.filter(user = request.user).first()
            # print(wishlist2.product_ver.first())
            wishlist2.product_ver.add(product)
            message = {'success': True, 'message' : 'Product added to your wishlist.'}
            return Response(message, status = status.HTTP_201_CREATED)
        message = {'success' : False, 'message': 'Product not found.'}
        return Response(message, status = status.HTTP_400_BAD_REQUEST)


    
class WishlistDeleteAPIView(APIView):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        ProductID = request.data.get('ProductID')
        Wishlist.objects.get(pk=ProductID).delete()
