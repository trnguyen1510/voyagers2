from django import forms
from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Profile
		fields = ('firstname', 'lastname', 'middlename', 'email', 'date_of_birth', 'twitter_handle', 'fb_handle', 'insta_handle', 'telephone', 'address1', 'address2', 'city', 'state', 'zipcode', 'profile_pic', 'about')


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['address1'].widget.attrs.update({'class' : 'form-group', 'placeholder': 'Enter Address Here'})