
from rest_framework import serializers
from django.db.models import fields
from .models import Tarea, Prioridad

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'descripcion','color', 'f_deseada', 'prioridad']

class PrioridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prioridad
        fields = '__all__'