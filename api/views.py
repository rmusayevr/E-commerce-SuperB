from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from Product.models import Product, Product_version
from Core.models import Subscription
from Order.models import Wishlist, basket
from .serializers import (
                    ProductReadSerializer, 
                    ProductVersionReadSerializer,
                    SubscriberSerializer,
                    WishlistSerializer,
                    BasketSerializer
                )
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

class ProductAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer

class ProductVersionAPI(ListAPIView):
    queryset = Product_version.objects.all()
    serializer_class = ProductVersionReadSerializer

class SubscriberAPI(ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriberSerializer

class WishlistAPI(APIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']

    def get(self, request, *args, **kwargs):
        obj, created = Wishlist.objects.get_or_create(user = request.user)
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')[0]
        product = Product.objects.filter(pk=product_id).first()
        if product:
            wishlist, created = Wishlist.objects.get_or_create(user = request.user)
            wishlist2 = Wishlist.objects.filter(user = request.user).first()
            wishlist2.product_ver.add(product)
            message = {'success': True, 'message' : 'Product added to your wishlist.'}
            return Response(message, status = status.HTTP_201_CREATED)
        message = {'success' : False, 'message': 'Product not found.'}
        return Response(message, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        ProductID = request.data.get('product')[0]
        if ProductID:
            user_wishlist =  Wishlist.objects.filter(user = self.request.user).first()
            product = user_wishlist.product_ver.filter(id = ProductID[0])
            user_wishlist.product_ver.remove(product[0].id)
        return Response(status = status.HTTP_200_OK)

class BasketAPI(APIView):
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']

    def get(self, request, *args, **kwargs):
        obj, created = basket.objects.get_or_create(user = request.user, is_active = True)
        basket1 = basket.objects.filter(Q(user = request.user), Q(is_active = True)).all()
        if len(basket1) != 1:
            basket1.last().delete()
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')[0]
        product = Product.objects.filter(pk=product_id).first()
        if product:
            for_basket, created = basket.objects.get_or_create(user = request.user, is_active = True)
            basket2 = basket.objects.filter(Q(user = request.user), Q(is_active = True)).first()
            product.quantity += 1
            product.save()
            basket2.product.add(product)
            message = {'success': True, 'message' : 'Product added to your wishlist.'}
            return Response(message, status = status.HTTP_201_CREATED)
        message = {'success' : False, 'message': 'Product not found.'}
        return Response(message, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        ProductID = request.data.get('product')[0]
        if ProductID:
            user_basket =  basket.objects.filter(user = self.request.user, is_active = True).first()
            product_s = Product.objects.filter(pk=ProductID).first()
            product_s.get_subtotal()
            product_s.quantity = 0
            product_s.save()
            product = user_basket.product.filter(id = ProductID[0])
            user_basket.product.remove(product[0].id)

        return Response(status = status.HTTP_200_OK)

