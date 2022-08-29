from rest_framework.generics import ListAPIView, ListCreateAPIView
from Product.models import Product, Product_version
from Core.models import Subscription
from .serializers import (
                    ProductReadSerializer, 
                    ProductVersionSerializer,
                    SubscriberSerializer
                )

class ProductAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer

class ProductVersionAPI(ListAPIView):
    queryset = Product_version.objects.all()
    serializer_class = ProductVersionSerializer

class SubscriberAPI(ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriberSerializer