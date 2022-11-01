from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import send_mail
from SuperB.settings import EMAIL_HOST_USER
from Core.models import Subscriber
from Product.models import Product, Product_version
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_mail_to_subscriber():
    print("Mail sending.......")
    email_list = Subscriber.objects.values_list("email", flat=True)
    products = Product_version.objects.order_by("-review_count").all()[:3]
    message = render_to_string('email/email-subscribers.html', {
                "products" : products
            })
    subject = 'New Products From Our Website'
    from_email = EMAIL_HOST_USER
    for email in email_list:
        to_email = email
        send_mail(
            subject = subject,
            message=None,
            html_message = message,
            from_email = from_email,
            recipient_list = [to_email] ,
            fail_silently=True,
        )
    return "Mail has been sent........"
    

