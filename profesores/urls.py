from django.urls import path
from . import views

urlpatterns = [
    path('', views.portal_profesores, name="portal_profesores"),
    path('lista/', views.lista_profesores, name="lista_profesores"),
    path('agregar_profesor/', views.registrar_profesor, name="agregar_profesor")
]