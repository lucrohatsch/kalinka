from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Tarea
from .forms import nuevaTarea, customUserCreationForm
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
from .serializers import TareaSerializer
from rest_framework import viewsets



def home(request):
    return render(request, "home.html")

@login_required
def tablero(request):

    if request.method == "POST":
        nueva=nuevaTarea(data=request.POST)
        
        if nueva.is_valid():
            nueva_completa= nueva.save(commit=False)
            nueva_completa.autor=request.user
            nueva_completa.save()
        return redirect(to="Tablero")

    usuario=request.user
    hoy_p=Tarea.objects.filter(autor=usuario, prioridad=1, estado=1)
    hoy_f=Tarea.objects.filter(autor=usuario, prioridad=1, estado=2)
    tranca_p=Tarea.objects.filter(autor=usuario, prioridad=2, estado=1)
    tranca_f=Tarea.objects.filter(autor=usuario, prioridad=2, estado=2)
    podria_p=Tarea.objects.filter(autor=usuario, prioridad=3, estado=1)
    podria_f=Tarea.objects.filter(autor=usuario, prioridad=3, estado=2)

    nueva=nuevaTarea()

    return render(request, "tablero.html", {"hoy_p":hoy_p,
                                            "hoy_f":hoy_f,
                                            "tranca_p":tranca_p,
                                            "tranca_f":tranca_f,
                                            "podria_p":podria_p,
                                            "podria_f":podria_f, 
                                            "nueva":nueva})
@login_required
def finalizarTarea(request, id):
    Tarea.objects.filter(id=id).update(f_cierre=datetime.now(), estado_id = 2)
    return redirect(to="Tablero")

@login_required
def borrarTarea(request,id):
    Tarea.objects.filter(id=id).delete()
    return redirect(to="Tablero")

class TareaViewst(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class= TareaSerializer

    def get_queryset(self):
        tareas = Tarea.objects.all()
        tarea_id=self.request.GET.get('id')
        if tarea_id:
            tareas=tareas.filter(id=tarea_id)
        
        return tareas

@login_required
def editarTarea(request, id):
    if request.method == "POST":
        tarea =  Tarea.objects.filter(id=id).first()
        data = request.POST
        tarea_serializer = TareaSerializer(tarea, data = data)
        if tarea_serializer.is_valid():
            tarea_serializer.save()
        return redirect(to="Tablero")


def registro(request):
    form=customUserCreationForm()

    if request.method=="POST":
        form=customUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            usuario=authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(request,usuario)
            return redirect(to="Home")
    return render(request, "registration/registro.html", {"form":form})