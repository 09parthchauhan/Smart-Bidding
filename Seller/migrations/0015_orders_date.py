# Generated by Django 4.0.2 on 2022-04-17 19:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0014_alter_orders_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]