from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    """ Список категорий """
    image = models.ImageField(
        'Изображение категория', upload_to='images/categories/', blank=True)
    name = models.CharField(
        'Имя категория', max_length=250)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'product_categories'

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']


class ProductTag(models.Model):
    """ Теги товара """
    name = models.CharField(
        'Имя тега', max_length=250, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        db_table = 'product_tags'


class Product(models.Model):
    """ Список товаров
    :extra = {..., 'volume_name': 'Объём'} """

    name = models.CharField(
        'Имя товара', max_length=250)

    tags = models.ManyToManyField(
        ProductTag, verbose_name='Теги', related_name='products', blank=True)
    extra = models.JSONField(
        'Доп. инф.', default=dict)

    created_dt = models.DateTimeField(auto_now=True)
    updated_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'products'

    def __str__(self):
        return self.name


class ProductPrice(models.Model):
    product = models.ForeignKey(
        Product, verbose_name='Товар', related_name='prices', on_delete=models.PROTECT)
    value = models.CharField(
        'Значение объёма', max_length=250, blank=True)
    quantity = models.IntegerField(
        'Количество', default=1)
    price = models.DecimalField(
        'Цена', max_digits=12, decimal_places=0)

    class Meta:
        verbose_name = 'Цена товара'
        verbose_name_plural = 'Цена товаров'
        db_table = 'products_prices'


class ProductImage(models.Model):
    """ Изображения вариации товара """
    product = models.ForeignKey(
        Product, verbose_name='Товар', related_name='images', on_delete=models.PROTECT)
    image = models.ImageField(
        'Изображение', upload_to='images/products/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображение товаров'
        db_table = 'products_images'


class ProductPriceHistory(models.Model):
    """
    :extra = {'name': 'nVidia Geforce 1660 super' 'Объём': 6гб}
    """
    product = models.ForeignKey(
        Product, verbose_name='ID товара', related_name='histories', on_delete=models.SET_NULL, null=True)
    extra = models.JSONField(
        'Вариация', default=dict)
    price = models.DecimalField(
        'Цена', max_digits=12, decimal_places=0)
    created_dt = models.DateTimeField(
        'Дата изменения цены', auto_now=True)

    class Meta:
        verbose_name = 'История изменения цены товара'
        verbose_name_plural = 'Истории изменений цен товаров'
        db_table = 'products_price_histories'
