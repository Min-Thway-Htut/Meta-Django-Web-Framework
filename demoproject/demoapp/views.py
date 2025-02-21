from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return HttpResponse("Hello, World!")

def homepage(request):
    return HttpResponse("Hello, this is a home page.")

def display_data(request):
    data_joined = datetime.today().year
    return HttpResponse(data_joined)

def testing(request):
    path = request.path
    method = request.method
    content = '''
<center>
<h2>Testing Django Request Response Objects</h2>
<p>Request path: {}</p>
<p>Request method: {}</p>
</center>'''.format(path, method)
    return HttpResponse(content)


def menuitems(request, player):
    players = {
        'ronaldo': 'Portugese Player',
        'messi': 'Argentinean Player',
        'neymar': 'Brazilian Player',
    }

    description = players[player]

    return HttpResponse(f"<h2>{player}</h2>" + description)