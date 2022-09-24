# Generated by Django 4.0.6 on 2022-09-23 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_wishlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shipping_addresses',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='billing_addresses',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='basket_item',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_basket_item', to='Product.product_version'),
        ),
        migrations.AddField(
            model_name='basket_item',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_basket_item', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='basket',
            name='items',
            field=models.ManyToManyField(related_name='basket_items', to='Order.basket_item'),
        ),
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_basket', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address_information',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
