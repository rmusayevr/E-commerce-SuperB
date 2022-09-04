from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

# @admin.register(Category)
# class CategoryAdmin()
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Product_version)
admin.site.register(Images_of_product)
admin.site.register(Review)
admin.site.register(ProductStatistic)