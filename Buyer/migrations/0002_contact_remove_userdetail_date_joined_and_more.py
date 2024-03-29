# Generated by Django 4.0.2 on 2022-04-14 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Buyer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='is_buyer',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='is_seller',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='landmark',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='password',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='username',
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='photo',
            field=models.ImageField(default='user-profile.png', upload_to='user'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='sex',
            field=models.BooleanField(choices=[(True, 'Male'), (False, 'Female')], default='', null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='usr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
