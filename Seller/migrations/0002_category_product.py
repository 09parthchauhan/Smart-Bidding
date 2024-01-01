# Generated by Django 4.0.2 on 2022-03-15 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('sub_Categories', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_id2', models.CharField(default='', max_length=100)),
                ('seller', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('current_bid', models.IntegerField(default=0)),
                ('winning_bid', models.IntegerField(default=0)),
                ('winner', models.CharField(default='', max_length=100, null=True)),
                ('total_bid', models.IntegerField(default=0)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('bid_date', models.DateTimeField(null=True)),
                ('description', models.TextField()),
                ('pub_date', models.DateField(auto_now=True)),
                ('image1', models.ImageField(default='', null=True, upload_to='products')),
                ('image2', models.ImageField(blank=True, default='', null=True, upload_to='products')),
                ('image3', models.ImageField(blank=True, default='', null=True, upload_to='products')),
                ('image4', models.ImageField(blank=True, default='', null=True, upload_to='products')),
                ('image5', models.ImageField(blank=True, default='', null=True, upload_to='products')),
                ('image6', models.ImageField(blank=True, default='', null=True, upload_to='products')),
                ('category', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='Seller.category', verbose_name='Category')),
            ],
        ),
    ]
