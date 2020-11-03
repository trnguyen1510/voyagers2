from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .forms import UserRegisterForm
from django.contrib import messages


# Create your views here.
def index(request):
    # Render the HTML template index.html
    return render(request, 'index.html')


def about(request):
    return render(request, 'about-us.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['your_pass']
        user = auth.authenticate(username=username, password=pass1)
        if user:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['re_pass']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'UserName already Taken')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already Taken')

        elif pass1 != pass2:
            messages.info(request, 'confirm password is mismatched')

        else:
            user = User.objects.create_user(username=username, password=pass1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('login')
    return render(request, "signup.html")