from django.db import models

class Person(models.Model):
    Person_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class Menuitems(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=300)
    year = models.IntegerField()