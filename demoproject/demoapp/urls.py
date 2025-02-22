from django.urls import path
from . import views

urlpatterns = [
    path('players/<str:player>', views.menuitems),
    path('', views.index, name="index"),
    path('', views.homepage, name="homepage"),
    path('', views.display_data, name="display_data"),
    path('', views.testing, name="testing"),
    path('', views.current_datetime, name="current_datetime")
]  