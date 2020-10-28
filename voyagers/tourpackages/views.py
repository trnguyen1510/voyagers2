from django.shortcuts import render
from .models import *


# Create your views here.
def tours(request):
    attractions = Attraction.objects.all()
    context = dict(attraction=attractions)
    return render(request, 'tours.html', context)
