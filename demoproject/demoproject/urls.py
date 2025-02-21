from django.contrib import admin
from django.urls import path, include
from demoapp import views

urlpatterns = [
    path('', include("demoapp.urls")),
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage),
    path('display_data/', views.display_data),
    path('testing/', views.testing),
]
