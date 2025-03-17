from django.db import models
from django.contrib.auth.models import User
import uuid


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, Mystery)")


    def __str__(self):
        return self.name
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Book(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name