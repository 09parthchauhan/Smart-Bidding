# Generated by Django 4.0.2 on 2022-05-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0008_reviewrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrating',
            name='fn',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='reviewrating',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='reviewrating',
            name='ln',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]