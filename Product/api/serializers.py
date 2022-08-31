from rest_framework import serializers
from Product.models import Product, Product_version, Category
from Core.models import Subscription
from Order.models import Wishlist

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category 
        fields = [
            'id',
            'name',
        ]

class ProductReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product 
        fields = [
            'id', 
            'name', 
            'overview',
            'manufacturer',
            'category'
        ]

class ProductVersionSerializer(serializers.ModelSerializer):
    product = ProductReadSerializer()

    class Meta:
        model = Product_version
        fields = [
            'id', 
            'cover_image',
            'price', 
            'quantity', 
            'details',
            'color',    
            'discount', 
            'new_price', 
            'product'
        ]

class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = [
            'user',
            'product'
        ]

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'id', 
            'email'
        ]