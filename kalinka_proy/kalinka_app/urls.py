from django.urls import path
from django.urls.conf import include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="Home"),
]

#urlpatterns+=static(settings.)
