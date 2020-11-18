# from django.shortcuts import render, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Note that we didn't mention user field here.
        fields = ('middlename',
                  'telephone',
                  'website',
                  'occupation',
                  'date_of_birth',
                  'bio',
                  'twitter_handle',
                  'fb_handle',
                  'insta_handle',
                  'address1',
                  'address2',
                  'city',
                  'state',
                  'zipcode',
                  )
