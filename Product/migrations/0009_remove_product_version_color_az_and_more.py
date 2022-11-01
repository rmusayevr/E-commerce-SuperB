# Generated by Django 4.0.6 on 2022-10-01 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_product_details_az_product_details_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_version',
            name='color_az',
        ),
        migrations.RemoveField(
            model_name='product_version',
            name='color_en',
        ),
        migrations.AlterField(
            model_name='review',
            name='price_review',
            field=models.IntegerField(choices=[(2, '40'), (4, '80'), (3, '60'), (5, '100'), (1, '20')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='quality_review',
            field=models.IntegerField(choices=[(2, '40'), (4, '80'), (3, '60'), (5, '100'), (1, '20')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='value_review',
            field=models.IntegerField(choices=[(2, '40'), (4, '80'), (3, '60'), (5, '100'), (1, '20')]),
        ),
    ]
