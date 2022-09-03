# Generated by Django 4.0.6 on 2022-09-03 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0025_category_name_az_category_name_en_product_name_az_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='price_review',
            field=models.IntegerField(choices=[(2, '40'), (5, '100'), (3, '60'), (4, '80'), (1, '20')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='quality_review',
            field=models.IntegerField(choices=[(2, '40'), (5, '100'), (3, '60'), (4, '80'), (1, '20')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='value_review',
            field=models.IntegerField(choices=[(2, '40'), (5, '100'), (3, '60'), (4, '80'), (1, '20')]),
        ),
    ]