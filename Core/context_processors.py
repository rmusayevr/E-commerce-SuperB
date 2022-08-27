from django.conf import settings

from Core.forms import SubscriptionForm


def base_data(request):
    data = {}
    data["form"] = SubscriptionForm()
    return data