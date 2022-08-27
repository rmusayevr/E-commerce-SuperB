# Generated by Django 4.0.6 on 2022-08-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0015_remove_product_collection_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_version',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
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