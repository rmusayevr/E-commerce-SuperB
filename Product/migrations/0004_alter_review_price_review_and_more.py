# Generated by Django 4.0.6 on 2022-08-19 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_alter_review_price_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='price_review',
            field=models.IntegerField(choices=[(1, '20'), (3, '60'), (4, '80'), (5, '100'), (2, '40')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='quality_review',
            field=models.IntegerField(choices=[(1, '20'), (3, '60'), (4, '80'), (5, '100'), (2, '40')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='value_review',
            field=models.IntegerField(choices=[(1, '20'), (3, '60'), (4, '80'), (5, '100'), (2, '40')]),
        ),
    ]