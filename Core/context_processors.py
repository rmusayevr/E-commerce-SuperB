from Order.models import basket
from Product.models import Product
from django.db.models import Q
from django.shortcuts import render

def base_data(request):
    data = {}
    if request.user.is_authenticated:
        shopping_card = basket.objects.filter(user = request.user, is_active = True).last()
        if shopping_card:
            all_products = shopping_card.items.all()
            data["basket_items"] = all_products
    return data