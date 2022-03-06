from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Tarea, Prioridad
from .forms import nuevaTarea, customUserCreationForm, nuevaPrioridad
from datetime import datetime, date
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
from .serializers import TareaSerializer, PrioridadSerializer
from rest_framework import viewsets

from django.db.models import Count, F, Value, Q



def home(request):
    """Página de inicio. 
    Solo presenta el proyecto. 
    Disponible a clientes públicos"""

    return render(request, "home.html")

@login_required
def tablero(request):
    """Tablero de tareas. Disponible solo a usuarios registrados.
    En metodo GET muestra el tablero
    En metodo POST crea nuevas tareas
    """

    if request.method == "POST":
        nueva=nuevaTarea(data=request.POST)
        
        if nueva.is_valid():
            nueva_completa= nueva.save(commit=False)
            nueva_completa.autor=request.user
            nueva_completa.save()
        return redirect(to="Tablero")

    usuario=request.user
    prioridades = Prioridad.objects.filter(creador=usuario).order_by('valor')
    data = []
    for prioridad in prioridades:
        pendientes=Tarea.objects.filter(autor=usuario, prioridad=prioridad, estado=1)
        resueltas=Tarea.objects.filter(autor=usuario, prioridad=prioridad, estado=2)
        data.append({"prioridad":prioridad,
                    "pendientes":pendientes,
                    "resueltas":resueltas})
    
    nueva=nuevaTarea()
    hoy=date.today()
    return render(request, "tablero.html", {"data":data, "nueva":nueva, "hoy":hoy})

@login_required
def finalizarTarea(request, id):
    """
    Finalización de tareas y retorna a tablero
    Con ID de tarea se cierra a fecha actual.
    """
    Tarea.objects.filter(id=id).update(f_cierre=datetime.now(), estado_id = 2)
    return redirect(to="Tablero")

@login_required
def borrarTarea(request,id):
    """
    Eliminación de tareas y redirección a Tablero
    Utiliza metodo POST con id de tarea.
    En html hay un Modal de confirmación.
    """
    if request.method=="POST":
        Tarea.objects.filter(id=id).delete()
    return redirect(to="Tablero")

class TareaViewst(viewsets.ModelViewSet):
    """
    Corresponde a la API.
    Por metodo GET se consulta con ID de tarea y devuelve un JSON con toda la información.
    Se consume con JS para rellenar formularios
    Utilizada para eliminar y modificar tareas.
    """
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
    """
    Edita tareas por metodo POST con el ID
    Desde JS se completa el formulario del model con la API.
    """
    if request.method == "POST":
        tarea =  Tarea.objects.filter(id=id).first()
        data = request.POST
        tarea_serializer = TareaSerializer(tarea, data = data)
        if tarea_serializer.is_valid():
            tarea_serializer.save()
        return redirect(to="Tablero")

@login_required
def configuracion(request):
    """
    Configuraciones de usuario
    En metodo GET muestra tabla de prioridades ordenadas por valor y envia formulario vacio,
    En metodo POST crea nuevas prioridades
    """
    if request.method=='POST':
        nueva=nuevaPrioridad(data=request.POST)
        if nueva.is_valid():
            nueva_completa= nueva.save(commit=False)
            nueva_completa.creador=request.user
            nueva_completa.save()
            print(nueva_completa)
        return redirect(to='config')
            
    usuario = request.user
    """
    En SQL seria algo como...
    select prioridad, count(tareas) from prioridades where autor=usuario
    
    """
    prioridades = Prioridad.objects.filter(creador=usuario).annotate(cantidades=Count('tarea', filter=Q(creador=usuario))).order_by('valor')
    nueva=nuevaPrioridad()
    info_usuario = User.objects.get(username=usuario)


    return render(request, 'config.html', {"prioridades":prioridades, "nueva":nueva, 'info_usuario':info_usuario})


@login_required
def eliminaPrioridad(request, id):
    """
    Eliminación de prioridades y redirección a pagina de configuración
    Utiliza metodo POST con id de prioridad.
    En html hay un Modal de confirmación.
    """
    if request.method == "POST":
        Prioridad.objects.filter(id=id).delete()

    return redirect(to='config')


class PrioridadViewst(viewsets.ModelViewSet):
    """
    Clase correspondiente a la API. Con ID devuelve JSON de prioridad
    """
    queryset = Prioridad.objects.all()
    serializer_class= PrioridadSerializer

    def get_queryset(self):
        prioridades = Prioridad.objects.all()
        prioridad_id=self.request.GET.get('id')
        if prioridad_id:
            prioridad=prioridades.filter(id=prioridad_id)
        
        return prioridad


@login_required
def editarPrioridad(request, id):
    """
    Por  JS se obtiene de prioridad con API
    Se completa el form y se guarda por metodo POST.
    """
    if request.method == "POST":
        prioridad =  Prioridad.objects.filter(id=id).first()
        data = request.POST
        prioridad_serializer = PrioridadSerializer(prioridad, data = data)
        if prioridad_serializer.is_valid():
            prioridad_serializer.save()
        return redirect(to="config")
    

def registro(request):
    """
    Crear usuario por metodo POST.
    Formulario personalizado a partir del modelo DJANGO
    Hace un login y retorna a tablero
    """
    form=customUserCreationForm()

    if request.method=="POST":
        form=customUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            usuario=authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(request,usuario)
            return redirect(to="Home")
    return render(request, "registration/registro.html", {"form":form})