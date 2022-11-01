# Generated by Django 4.0.6 on 2022-10-01 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_image_alter_review_price_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='details_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='details_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='overview_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='overview_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product_version',
            name='color_az',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_color', to='Product.color'),
        ),
        migrations.AddField(
            model_name='product_version',
            name='color_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_color', to='Product.color'),
        ),
        migrations.AlterField(
            model_name='review',
            name='price_review',
            field=models.IntegerField(choices=[(5, '100'), (3, '60'), (1, '20'), (4, '80'), (2, '40')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='quality_review',
            field=models.IntegerField(choices=[(5, '100'), (3, '60'), (1, '20'), (4, '80'), (2, '40')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='value_review',
            field=models.IntegerField(choices=[(5, '100'), (3, '60'), (1, '20'), (4, '80'), (2, '40')]),
        ),
    ]