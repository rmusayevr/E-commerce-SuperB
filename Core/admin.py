from django.contrib import admin
from .models import FAQ, ContactUs, Subscription, BlockedIP

admin.site.register(FAQ)
admin.site.register(ContactUs)
admin.site.register(Subscription)
admin.site.register(BlockedIP)
