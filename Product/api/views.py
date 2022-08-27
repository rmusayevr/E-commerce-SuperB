from rest_framework.generics import ListAPIView
from Product.models import Product, Product_version
from .serializers import (
                    ProductReadSerializer, 
                    ProductVersionSerializer
                )

class ProductAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer

class ProductVersionAPI(ListAPIView):
    queryset = Product_version.objects.all()
    serializer_class = ProductVersionSerializer
