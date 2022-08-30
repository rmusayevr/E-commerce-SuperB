from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Product_version, ProductStatistic

@receiver(post_save, sender=Product_version)
def post_save_func(sender, instance, *args, **kwargs):
    ProductStatistic.objects.create(
        product = instance
    )

