from django.urls import path
from django.urls.conf import include
from . import views
from django.conf.urls.static import static
from rest_framework import routers
from django.contrib.auth import views as auth_views

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

    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),
    
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name="password_reset/password_change.html"), 
        name='password_change'),
    
    path('accounts/password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
        name='password_reset_done'),

    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset_form.html'), 
        name='password_reset'),
    
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
        name='password_reset_complete'),
]

