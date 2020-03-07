from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City never sleeps!'
    dest1.img = 'destination_1.jpg'
    dest1.price  = 1000
    dest1.offer  = False
    
    dest2 = Destination()
    dest2.name = 'Agra'
    dest2.desc = 'The City never sleeps!'
    dest2.img = 'destination_2.jpg'
    dest2.price  = 800
    dest2.offer = True

    dests = [dest1, dest2]

    return render(request, 'index.html', {'dests' : dests})
