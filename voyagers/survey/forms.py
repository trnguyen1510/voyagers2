from django import forms
from django.contrib.auth.models import User
from .models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question', 'option_one', 'option_two', 'option_three', 'option_four')