from django.urls import path
from . import views

urlpatterns = [
    path("", views.portal_cursos, name="portal_cursos"),
    path("lista/", views.lista_cursos, name="lista_cursos"),
    path("agregar_curso/", views.registrar_curso, name="agregar_cursos"),
]