from . import views
from django.urls import path
from django.contrib import admin
from .views import contact_view

urlpatterns = [
    path("contact/", contact_view, name="contact")
]

