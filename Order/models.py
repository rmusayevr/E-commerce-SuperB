from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from Product.models import Product

class address_information(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    street_address = models.CharField(max_length=150)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=150, null=True, blank=True)
    is_billing = models.BooleanField(default=False)
    is_shipping = models.BooleanField(default=False)  
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    zip = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name}'s address information"

    class Meta:
        verbose_name = "Address Information"
        verbose_name_plural = "Address Informations"

class billing_addresses(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    street_address = models.CharField(max_length=150)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=150, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    zip = models.IntegerField()

    def __str__(self):
        return f"{self.first_name}'s billing address"

    class Meta:
        verbose_name = "Billing Address"
        verbose_name_plural = "Billing Addresses"

class shipping_addresses(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    street_address = models.CharField(max_length=150)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=150, null=True, blank=True)
    # province = models.ForeignKey("province", on_delete=models.CASCADE, null=True)  
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    zip = models.IntegerField()
     
    def __str__(self):
        return f"{self.first_name}'s shipping address"

    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Addresses"

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_wishlist")
    product_ver = models.ManyToManyField(Product, related_name="products_wishlist")

    def __str__(self):
        return f"{self.user}'s wishlist"

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"   

class basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ManyToManyField(Product, related_name="products_basket")

    def __str__(self):
        return f"{self.user.username}'s basket"

    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"