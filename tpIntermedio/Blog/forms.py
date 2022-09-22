
from re import template
from socket import fromshare
from django import forms

class formCreacionEditor(forms.Form):
    username = forms.CharField(max_length=30)
    mail = forms.EmailField()
    edad = forms.IntegerField()

class formCreacionLector(forms.Form):
    username = forms.CharField(max_length=30)
    mail = forms.EmailField()
    edad = forms.IntegerField()

class formCreacionIdea(forms.Form):
    tema = forms.CharField(max_length=30)
    texto = forms.CharField(max_length=280)
    autor = forms.CharField(max_length=30)
