from colorfield.fields import ColorField
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Prioridad(models.Model):
    nombre=models.CharField(max_length=10)
    valor=models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    creador=models.ForeignKey(User, on_delete=CASCADE, default=1)

    class Meta:
        verbose_name="prioridad"
        verbose_name_plural="prioridades"
        ordering = ['valor']
    
    def __str__(self):
        prioridad_json = {"id":self.id,
                          "nombre":self.nombre,
                          "creador":self.creador,
                          "valor":self.valor}
        return self.nombre

class Estado(models.Model):
    nombre=models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name="estado"
        verbose_name_plural="estados"
    
    def __str__(self):

        return self.nombre

class Tarea(models.Model):
    autor=models.ForeignKey(User, on_delete=CASCADE)
    titulo=models.CharField(max_length=50, blank=False)
    descripcion=models.TextField(blank=True, null=True)
    prioridad=models.ForeignKey(Prioridad, null=True, on_delete=SET_NULL)
    color = ColorField(default='#FF0000')
    estado=models.ForeignKey(Estado, null=True, default=1, on_delete=SET_NULL)
    f_creacion=models.DateField(auto_now_add=True)
    f_deseada=models.DateField()
    f_cierre=models.DateField(blank=True, null=True)

    class Meta:
        verbose_name="tarea"
        verbose_name_plural="tareas"
    
    
    def __str__(self):
        tarea_json={
            "titulo":self.titulo, 
            "descripcion":self.descripcion, 
            "prioridad":self.prioridad,
            "color":self.color,
            "f_deseada":self.f_deseada}
        
        return str(tarea_json)
