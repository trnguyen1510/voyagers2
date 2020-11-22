from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from .models import *
from .forms import *
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
# Create your views here.

@login_required()
def survey(request):
    return render(request, 'surveyhome.html') #need to create surveyhome.html or do it in dashboard?

def vote(request，question_id):
    pk = request.user.pk
    question = User.objects.get(pk=pk)

