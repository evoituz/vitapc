from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    """ Авторизация по email or phone """

    avatar = models.ImageField(
        'Аватарка', upload_to='images/users/avatars/', null=True)
    name = models.CharField(
        'Имя', max_length=250, blank=True)
    birthday = models.DateField(
        'Дата рождения', blank=True)
    gender = models.CharField(
        'Пол', max_length=50, blank=True)
    address = models.CharField(
        'Адрес', max_length=250, blank=True)
    phone = models.CharField(
        'Телефон', max_length=250, unique=True)

    phone_verified = models.BooleanField(
        'Верифицированный номер', default=False)

    USERNAME_FIELD = 'username'
    objects = UserManager()
    REQUIRED_FIELDS = ['phone']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'
