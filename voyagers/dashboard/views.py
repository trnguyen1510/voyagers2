from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForm

# Create your views here.


def dashboard(request):
    #fetch data from mongo and display
    profiles = Profile.objects.order_by('id')

    context = {'profiles': profiles}
    
    # Render the HTML template index.html
    return render(request, 'dashboard.html', context)

def editing(request):

    #update mongo user details with user's changes
    if request.method == 'POST':
        form = ProfileForm(request.POST)
    
        if form.is_valid():
            form.save()
            return redirect('dashboard.html')
    else:
        form = ProfileForm()
        context = {'form': form}

    return render(request, 'editing.html', context)