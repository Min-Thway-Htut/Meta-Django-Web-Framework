from django.db import models

class Person(models.Model):
    Person_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

