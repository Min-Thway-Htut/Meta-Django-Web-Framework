from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime
from .models import Menu

def about(request):
    return render(request, "about.html")

#def menu(request):
#    newmenu = {
#        'mains': [
#            {'name': 'Falafel', 'price': "12"},
#            {'name': 'shawarma', 'price': '15'},
#            {'name': 'gyro', 'price': '10'},
#    ]}
#    return render(request, 'menu.html', newmenu)


def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu': newmenu}
    return render(request, 'menu_card.html', newmenu_dict)



