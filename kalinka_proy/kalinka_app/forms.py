from django import forms
from django.forms import fields, widgets
from .models import Tarea, Prioridad
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class nuevaTarea(forms.ModelForm):
    color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color', 'value': '#ffffff', 'class': 'form-control-color'}))
        
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'prioridad', 'color', 'f_deseada']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.Textarea(attrs={'class': 'form-control'}),
            'prioridad':forms.Select(attrs={'class': 'form-control'}),
            'f_deseada':forms.TextInput(attrs={'type': 'date', 'class': 'form-control'})
        }

class customUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
    
class nuevaPrioridad(forms.ModelForm):
    nombre=forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}))
    valor=forms.IntegerField(label="", widget=forms.TextInput(attrs={'placeholder': 'valor', 'type':'number', 'max':'10', 'class': 'form-control'}))
    class Meta:
        model=Prioridad
        fields=['nombre', 'valor']
        
