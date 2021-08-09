from apps.libro.views import Home, crearAutor, editarAutor, eliminarAutor, listarAutor
from django.urls import path

urlpatterns = [
    path('crear_autor/',crearAutor,name='crear_autor'),
    path('listar_autor/',listarAutor,name='listar_autor'),
    path('editar_autor/<int:id>',editarAutor, name='editar_autor'),
    path('eliminar_autor/<int:id>',eliminarAutor,name='eliminar_autor'),
]