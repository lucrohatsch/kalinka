from django.urls import path
from django.urls.conf import include
from . import views
from django.conf.urls.static import static
from rest_framework import routers

router=routers.DefaultRouter()
router.register('tarea', views.TareaViewst)
router.register('prioridad', views.PrioridadViewst)


urlpatterns = [
    path('', views.home, name="Home"),
    path('tablero/', views.tablero, name="Tablero"),
    path('tablero/finalizarTarea/<id>', views.finalizarTarea, name="finalizarTarea"),
    path('tablero/borrarTarea/<id>', views.borrarTarea, name="borrarTarea"),
    path('registro/', views.registro, name="Registro"),
    path('tablero/editarTarea/<id>', views.editarTarea, name="editarTarea"),
    path('api/', include(router.urls), name="api"),
    path('config/', views.configuracion, name='config'),
    path('config/eliminaPrioridad/<id>', views.eliminaPrioridad, name='eliminaPrioridad'),
    path('config/editarPrioridad/<id>', views.editarPrioridad, name="editarPrioridad"),
]

