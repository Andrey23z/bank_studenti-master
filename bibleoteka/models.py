from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save


class Author(models.Model):
    class Meta:
        verbose_name = 'Авторы'
        verbose_name_plural = 'Авторы'

    name = models.CharField('Имя', db_index=True, max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Genre(models.Model):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанр'

    name = models.CharField('Название', db_index=True, max_length=255, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'

    name = models.CharField('Название', db_index=True, max_length=255, unique=True)
    genre = models.ForeignKey(Genre, verbose_name='Жанр', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class AuthorBook(models.Model):
    class Meta:
        verbose_name = 'Авторы'
        verbose_name_plural = 'Авторы'

    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.PROTECT)
    book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.PROTECT)

    def __str__(self):
        return self.id

class City(models.Model):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Город'

    name = models.CharField('Название', db_index=True, max_length=255, unique=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
        class Meta:
            verbose_name = 'Покупатели'
            verbose_name_plural = 'Покупатели'

        name = models.CharField('Название', db_index=True, max_length=255, unique=True)
        address = models.CharField('Адресс', db_index=True, max_length=255)
        phone = models.CharField('Контактный телефон', db_index=True, null=True, blank=True, max_length=255)

        def __str__(self):
            return self.name


class Suppliers(models.Model):
    class Meta:
        verbose_name = 'Поставщики'
        verbose_name_plural = 'Поставщики'

    name = models.CharField('Имя', db_index=True, max_length=255, unique=True)
    address = models.CharField('Адресс', db_index=True, max_length=255)
    inn = models.CharField('ИНН', db_index=True, max_length=255)
    fax = models.CharField('ИНН', db_index=True, max_length=255)

    def __str__(self):
        return self.name

class Delivery(models.Model):
    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'

    suppliers = models.ForeignKey(Suppliers, verbose_name='Поставщик', on_delete=models.PROTECT)
    city = models.ForeignKey(City, verbose_name='Автор', on_delete=models.PROTECT)
    date = models.DateField('Дата доставки', blank=True, null=True)

    def __str__(self):
        return self.date


class Employees(models.Model):
    class Meta:
        verbose_name = 'Работники'
        verbose_name_plural = 'Работники'

    name = models.CharField('Имя', db_index=True, max_length=255, unique=True)
    address = models.CharField('Адресс', db_index=True, max_length=255)
    phone = models.CharField('Контактный телефон', db_index=True, null=True, blank=True, max_length=255)
    birthday = models.DateField('Дата рождения', blank=True, null=True)

    def __str__(self):
        return self.name

class Treaty(models.Model):
    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договор'

    customer = models.ForeignKey(Customer, verbose_name='Покупатель', on_delete=models.PROTECT)
    date = models.DateField('Дата договора', blank=True, null=True)

    def __str__(self):
        return self.date

class Order(models.Model):
     class Meta:
         verbose_name = 'Заказ'
         verbose_name_plural = 'Заказ'

     customer = models.ForeignKey(Customer, verbose_name='Покупатель', on_delete=models.PROTECT)
     date = models.DateField('Дата заказа', blank=True, null=True)
     treaty = models.ForeignKey(Treaty, verbose_name='Договор', on_delete=models.PROTECT)
     employees = models.ForeignKey(Employees, verbose_name='Работник', on_delete=models.PROTECT)

     def __str__(self):
       return self.date


class OrderBook(models.Model):
    class Meta:
        verbose_name = 'Заказ_книг'
        verbose_name_plural = 'Заказ_книг'

    customer = models.ForeignKey(Customer, verbose_name='Покупатель', on_delete=models.PROTECT)
    book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.PROTECT)
    date_vozvrata = models.DateField('Дата заказа', blank=True, null=True)

    def __str__(self):
        return self.date_vozvrata


class Purchase(models.Model):
    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупка'

    book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, verbose_name='Покупатель', on_delete=models.PROTECT)
    price = models.CharField('Цена', null=True, blank=True, max_length=10, db_index=True)
    date = models.DateField('Дата покупки', blank=True, null=True)

    def __str__(self):
        return self.price

class OrderDetails(models.Model):
    class Meta:
        verbose_name = 'Детали_заказа'
        verbose_name_plural = 'Детали_заказа'

    book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.PROTECT)
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.PROTECT)
    count = models.CharField('Количество', null=True, blank=True, max_length=10, db_index=True)
    purchase = models.ForeignKey(Purchase, verbose_name='Покупка', on_delete=models.PROTECT)

    def __str__(self):
        return self.count



class Stock(models.Model):
    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'

    book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.PROTECT)
    delivery = models.ForeignKey(Delivery, verbose_name='Доставка', on_delete=models.PROTECT)

    def __str__(self):
        return self.id




