from django.contrib import admin
from .models import billing_addresses, shipping_addresses, address_information, Wishlist, basket, order

admin.site.register(order)
admin.site.register(basket)
admin.site.register(billing_addresses)
admin.site.register(shipping_addresses)
admin.site.register(address_information)
admin.site.register(Wishlist)