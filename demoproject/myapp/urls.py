from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('home/', views.form_view)
]

