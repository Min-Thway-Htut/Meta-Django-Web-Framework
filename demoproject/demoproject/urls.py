from django.contrib import admin
from django.urls import path, include
from demoapp import views
from myapp import views

urlpatterns = [
    path('',include('demoapp.urls')),
    path('admin/', admin.site.urls),
]


