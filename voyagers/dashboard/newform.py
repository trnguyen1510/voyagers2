from django import forms

class Userform(forms.Form):
    username = form.CharField(label = 'What is your name', max_length=30)

