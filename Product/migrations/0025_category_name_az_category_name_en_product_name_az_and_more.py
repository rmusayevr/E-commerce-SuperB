# Generated by Django 4.0.6 on 2022-09-03 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0024_alter_review_price_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
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
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product_version',
            name='color_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product_version',
            name='details_az',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product_version',
            name='details_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='price_review',
            field=models.IntegerField(choices=[(5, '100'), (1, '20'), (3, '60'), (4, '80'), (2, '40')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='quality_review',
            field=models.IntegerField(choices=[(5, '100'), (1, '20'), (3, '60'), (4, '80'), (2, '40')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='value_review',
            field=models.IntegerField(choices=[(5, '100'), (1, '20'), (3, '60'), (4, '80'), (2, '40')]),
        ),
    ]