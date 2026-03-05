from django.urls import path
from . import views

urlpatterns = [
    path('', views.portal_alumnos, name='portal_alumnos'),
    path('lista/', views.lista_alumnos, name='lista_alumnos'),
    path('agregar_alumno/', views.agregar_alumno, name='agregar_alumno')
]