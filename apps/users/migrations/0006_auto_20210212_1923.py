# Generated by Django 3.1.6 on 2021-02-12 14:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, max_length=10, verbose_name='Код для подтверждения'),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_dt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата и время получения кода'),
            preserve_default=False,
        ),
    ]
