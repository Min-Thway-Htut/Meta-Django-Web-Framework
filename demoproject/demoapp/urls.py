from django.urls import path, include
from . import views

urlpatterns = [
    path('about/', views.about),
    path('menu_card/', views.Menu),

]