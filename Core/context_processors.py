from Order.models import basket
from Core.forms import SubscriptionForm

def base_data(request):
    data = {}
    data["subscriber_form"] = SubscriptionForm()
    if request.user.is_authenticated:
        user_wishlist =  basket.objects.filter(user = request.user, is_active = True).last()
        if user_wishlist:
            all_products = user_wishlist.product.all()
            data["basket_items"] = all_products
    return data