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

class ProductVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_version
        fields = [
            'id', 
            'color',    
        ]

class ProductReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    product = serializers.SerializerMethodField()

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
            'category'
        ]

    def get_product(self, obj):
        serializer = ProductVersionSerializer(obj.recipes.all(), context=self.context, many=True)
        return serializer.data


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