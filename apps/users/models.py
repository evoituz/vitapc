from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from apps.products.models import Product, ProductPrice


class User(AbstractUser):
    """ Авторизация по email or phone """

    avatar = models.ImageField(
        'Аватарка', upload_to='images/users/avatars/', blank=True, null=True)
    name = models.CharField(
        'Имя', max_length=250, blank=True)
    birthday = models.DateField(
        'Дата рождения', blank=True, null=True)
    gender = models.CharField(
        'Пол', max_length=50, blank=True)
    address = models.CharField(
        'Адрес', max_length=250, blank=True)
    phone = models.CharField(
        'Телефон', max_length=250, unique=True)
    balance = models.DecimalField(
        'Баланс', max_digits=20, decimal_places=0, default=0)

    phone_verified = models.BooleanField(
        'Верифицированный номер', default=False)

    USERNAME_FIELD = 'username'
    objects = UserManager()
    REQUIRED_FIELDS = ['phone']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'


class CartItem(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Пользователь', related_name='cart_items', on_delete=models.PROTECT)
    product = models.ForeignKey(
        Product, verbose_name='Товар', related_name='carts', on_delete=models.CASCADE)
    product_price = models.ForeignKey(
        ProductPrice, verbose_name='Цена товара', related_name='carts', on_delete=models.CASCADE)
    quantity = models.IntegerField(
        'Количество', default=1)
    extra = models.JSONField(
        'Доп. инф.', null=True, blank=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        db_table = 'users_cart_items'
