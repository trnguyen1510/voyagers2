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
        min_length = 8

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['re_pass']
        first_isalpha = pass1[0].isalpha()

        if User.objects.filter(username=username).exists():
            messages.info(request, 'UserName is already Taken')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email is already Taken')
        elif len(pass1) < min_length:
            messages.info(request, 'The new password must be at least %d characters long.' % min_length)
        elif all(c.isalpha() == first_isalpha for c in pass1):
            messages.info(request, 'The new password must contain at least one letter and at least one digit or '
                                   'punctuation character')
        elif pass1 != pass2:
            messages.info(request, 'Password and confirm password do not match')

        else:
            user = User.objects.create_user(username=username, password=pass1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('login')
    return render(request, "signup.html")