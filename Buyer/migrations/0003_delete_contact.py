# Generated by Django 4.0.2 on 2022-04-14 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0002_contact_remove_userdetail_date_joined_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
