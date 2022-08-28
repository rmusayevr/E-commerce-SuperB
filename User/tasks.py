from celery import shared_task
from Core.models import Subscription
from Product.models import Product_version
from django.template.loader import render_to_string

@shared_task
def send_email_to_subscribers():
    email_list = Subscription.objects.values_list("email", flat=True)
    products = Product_version.objects.all()
    message = render_to_string('email/email-subscribers.html', {
                "products" : products
            })
    subject = 'New Products From Our Website'
    