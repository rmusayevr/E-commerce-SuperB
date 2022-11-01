# Generated by Django 4.0.6 on 2022-10-30 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_remove_product_version_color_az_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='price_review',
            field=models.IntegerField(choices=[(5, '100'), (3, '60'), (2, '40'), (1, '20'), (4, '80')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='quality_review',
            field=models.IntegerField(choices=[(5, '100'), (3, '60'), (2, '40'), (1, '20'), (4, '80')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='value_review',
            field=models.IntegerField(choices=[(5, '100'), (3, '60'), (2, '40'), (1, '20'), (4, '80')]),
        ),
    ]
