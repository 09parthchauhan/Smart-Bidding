# Generated by Django 4.0.2 on 2022-04-17 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0015_orders_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellerdetail',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='sellerdetail',
            name='landmark',
        ),
    ]
