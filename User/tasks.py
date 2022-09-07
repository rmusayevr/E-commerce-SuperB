from celery import shared_task
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from Core.models import Subscription
from Product.models import Product

@shared_task
def send_email_to_subscribers():
    email_list = Subscription.objects.values_list("email", flat=True)
    products = Product.objects.all()
    message = render_to_string('email/email-subscribers.html', {
                "products" : products
            })
    subject = 'New Products From Our Website'
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
    mail.content_subtype = 'html'
    mail.send()

    