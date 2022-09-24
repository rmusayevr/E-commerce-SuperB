# Generated by Django 4.0.6 on 2022-09-24 06:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_alter_review_price_review_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
        migrations.AddField(
            model_name='product_version',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='price_review',
            field=models.IntegerField(choices=[(1, '20'), (3, '60'), (2, '40'), (4, '80'), (5, '100')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='quality_review',
            field=models.IntegerField(choices=[(1, '20'), (3, '60'), (2, '40'), (4, '80'), (5, '100')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='value_review',
            field=models.IntegerField(choices=[(1, '20'), (3, '60'), (2, '40'), (4, '80'), (5, '100')]),
        ),
    ]