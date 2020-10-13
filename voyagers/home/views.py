from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
# Render the HTML template index.html
    return render(request, 'index.html')

def about(request):
    return render(request,'about-us.html')

def login(request):
    return render(request,'login.html')    

def signup(request):
    return render(request,'signup.html')        