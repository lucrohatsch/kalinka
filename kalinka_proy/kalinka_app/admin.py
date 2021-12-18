from django.contrib import admin
from .models import Prioridad, Estado, Tarea
# Register your models here.

class TareaAdmin(admin.ModelAdmin):
    readonly_fields=('f_creacion','f_cierre')

admin.site.register(Prioridad)
admin.site.register(Estado)
admin.site.register(Tarea, TareaAdmin)
