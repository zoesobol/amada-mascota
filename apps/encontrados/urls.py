from django.urls import path
from .views import publicar, lista_encontrados, editar_publicacion, publicacion, eliminar_publicacion, renovar_publicacion
from .views import buscar_e

app_name = 'encontrados'

urlpatterns = [
   path('publicar/', publicar, name='publicar'),
   path('listar/', lista_encontrados, name='lista_encontrados'),
   path('editar/<id_publicacion>/', editar_publicacion, name='editar_publicacion'),
   path('borrar/<id_publicacion>/', eliminar_publicacion, name='eliminar_publicacion'),
   path('buscar_e/', buscar_e, name='buscar_e'),
   path('publicacion/<id_publicacion>/', publicacion, name='publicacion'),  
   path('renovar/<id_publicacion>/', renovar_publicacion, name='renovar_publicacion'),
   #path('lista_encontrados', lista_encontrados, name='lista_encontrados'),
   #path('editar/<id>', editar_publicacion, name='editar_publicacion'),
   #path('resultado-busqueda/', buscar, name='buscar'),
]
 #  path('resultado-busqueda/', buscar, name='buscar'),


