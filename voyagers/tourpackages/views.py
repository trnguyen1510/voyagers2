from django.shortcuts import render

# Create your views here.
def tours(request):
    context = {}
    return render(request, 'tours.html')
