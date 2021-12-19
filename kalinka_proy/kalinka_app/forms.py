from django import forms
from django.forms import fields, widgets
from .models import Tarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class nuevaTarea(forms.ModelForm):
    color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    f_deseada = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'prioridad', 'color', 'f_deseada']

class customUserCreationForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
    
