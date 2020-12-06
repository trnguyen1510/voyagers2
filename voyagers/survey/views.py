from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import Survey
# from .forms import *
# from django.forms.models import inlineformset_factory
# from django.core.exceptions import PermissionDenied
import json
from django.http import HttpResponse
from dashboard.forms import UserForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

# Create your views here.


@login_required()
def survey(request):
    pk = request.user.pk
    user = User.objects.get(pk=pk)
    user.save()

    



    return render(request, 'survey.html')
    # form = UserForm(instance=user)

    # ProfileInlineFormset = inlineformset_factory(User, surveyForm, fields=('country',
    #                                                                    'city',
    #                                                                    'tour',
    #                                                                    'departure',))
    # formset = ProfileInlineFormset(instance=user)
    # if request.user.is_authenticated and request.user.id == user.id:
    #     if request.method == "POST":
    #         form = UserForm(request.POST, instance=request.user)
    #         formset = ProfileInlineFormset(
    #             request.POST, request.FILES, instance=user)

    #         if form.is_valid():
    #             custom_form = form.save(commit=False)
    #             formset = ProfileInlineFormset(
    #                 request.POST, request.FILES, instance=custom_form)
    #             if formset.is_valid():
    #                 custom_form.save()
    #                 formset.save()
    #                 return redirect('dashboard')

    #     return render(request, 'survey.html', {
    #         "pk": pk,
    #         "formset": formset,
    #     })
    # else:
    #     raise PermissionDenied
