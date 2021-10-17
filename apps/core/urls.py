from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('categoria/', categoria_add, name='add_categoria'),
    path('sitio/', sitio_add, name='add_sitio'),
    path('categoria/<int:id_categoria>', categoria_list, name='lista_categoria'),
    path('sitio/<int:id_sitio>/', sitio, name='sitio'),
]
