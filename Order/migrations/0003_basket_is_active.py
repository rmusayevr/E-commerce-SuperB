# Generated by Django 4.0.6 on 2022-09-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
