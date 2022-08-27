from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# class country(models.Model):
#     name = models.CharField(max_length=50)
#     code = models.CharField(max_length=2)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Country"
#         verbose_name_plural = "Countries"

# class city(models.Model):
#     name = models.CharField(max_length=50)
#     city_code = models.CharField(max_length=4)
#     country = models.ForeignKey("country", on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name = "City"
#         verbose_name_plural = "Cities"

# class province(models.Model):
#     name = models.CharField(max_length=150)
#     city = models.ForeignKey("city", on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Province"
#         verbose_name_plural = "Provinces"

class address_information(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    street_address = models.CharField(max_length=150)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=150, null=True, blank=True)
    # province = models.ForeignKey("province", on_delete=models.CASCADE, null=True)  
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
    # province = models.ForeignKey("province", on_delete=models.CASCADE, null=True)  
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

class basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s basket"

    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"