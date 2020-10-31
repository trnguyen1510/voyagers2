from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.db.models import Q


# Create your views here.
def tours(request):
    attractions = Attraction.objects.all()
    context = dict(attraction=attractions)
    return render(request, 'tours.html', context)

# class tours(ListView):
#     model = Attraction
#     template_name = 'tours.html'

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         attraction = Attraction.objects.filter(
#             Q(city__icontains=query))
#         return attraction
