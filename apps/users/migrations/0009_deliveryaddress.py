# Generated by Django 3.1.6 on 2021-02-15 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210215_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='Адрес')),
                ('lat', models.CharField(blank=True, max_length=250, verbose_name='Latitude')),
                ('long', models.CharField(blank=True, max_length=250, verbose_name='Longitude')),
                ('phone', models.CharField(blank=True, max_length=250, verbose_name='Номер телефона')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_addresses', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Адрес доставки',
                'verbose_name_plural': 'Адреса доставки',
                'db_table': 'delivery_addresses',
            },
        ),
    ]