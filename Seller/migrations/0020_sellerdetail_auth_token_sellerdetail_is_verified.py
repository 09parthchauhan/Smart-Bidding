# Generated by Django 4.1.7 on 2023-04-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0019_delete_paytmhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerdetail',
            name='auth_token',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='sellerdetail',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]