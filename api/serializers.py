from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method
from Product.models import Product, Product_version, Category
from Core.models import Subscription
from Order.models import Wishlist

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category 
        fields = [
            'id',
            'name',
            'p_category'
        ]

class ProductVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_version
        fields = [
            'id', 
            'color',    
        ]

class ProductReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    product_ver = serializers.SerializerMethodField()

    class Meta:
        model = Product 
        fields = [
            'id', 
            'name', 
            'overview',
            'details',
            'cover_image',
            'manufacturer',
            'price', 
            'discount', 
            'new_price', 
            'category',
            'product_ver'
        ]

    @swagger_serializer_method(serializer_or_field=ProductVersionSerializer(many=True))
    def get_product_ver(self, obj):
        return ProductVersionSerializer().data

class ProductVersionReadSerializer(serializers.ModelSerializer):
    product = ProductReadSerializer()

    class Meta:
        model = Product_version
        fields = [
            'id', 
            'color',    
            'quantity',
            'product'
        ]

class WishlistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Wishlist
        fields = [
            'user',
            'product_ver'
        ]

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'id', 
            'email'
        ]