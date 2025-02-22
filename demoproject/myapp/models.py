from django.db import models

class Person(models.Model):
    Person_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class Menuitems(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=300)
    year = models.IntegerField()

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

class Menu(models.Model):
    menu_item = models.CharField(max_length = 200)
    price = models.IntegerField(null = False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)

class Customer(models.Model):
    name = models.CharField(max_length=255)

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='Vehicle'
    )