# Generated by Django 4.0.2 on 2022-05-05 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0018_orders_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaytmHistory',
        ),
    ]