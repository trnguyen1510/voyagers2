from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import *
# from .forms import *
# from django.forms.models import inlineformset_factory
# from django.core.exceptions import PermissionDenied
from tourpackages.models import Attraction
import json
from django.http import HttpResponse
# Create your views here.


@login_required()
def survey(request):


   
    return render(request, 'survey.html')


