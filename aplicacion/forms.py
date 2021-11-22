from django.db.models import fields
from django.forms import ModelForm
from django import forms
from django.forms.widgets import TextInput
from aplicacion.models import *

class Usuarioform(forms.Form):
    usuario=forms.CharField(max_length=30, widget=forms.TextInput(attrs={
         'class': "form-control form-control-sm",
          }))
    correo=forms.CharField(max_length=30, widget=forms.EmailInput(attrs={
         'class': "form-control form-control-sm",
          }))
    password1=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
         'class': "form-control form-control-sm",
         }))
    password2=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
         'class': "form-control form-control-sm",
         }))

class Entrarform(forms.Form):
     usuario=forms.CharField(max_length=30, widget=forms.TextInput(attrs={
         'class': "form-control form-control-sm",
          }))
     password=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
         'class': " form-control form-control-sm",
         }))


