from django.contrib import admin
from .models import billing_addresses, shipping_addresses, address_information

# admin.site.register(province)
# admin.site.register(city)
# admin.site.register(country)
# admin.site.register(basket)
admin.site.register(billing_addresses)
admin.site.register(shipping_addresses)
admin.site.register(address_information)
