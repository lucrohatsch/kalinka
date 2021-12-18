from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="Home"),
    path('tablero/', views.tablero, name="Tablero"),
    path('tablero/finalizarTarea/<id>', views.finalizarTarea, name="finalizarTarea"),
    path('tablero/borrarTarea/<id>', views.borrarTarea, name="borrarTarea"),
    path('registro/', views.registro, name="Registro"),
]

