from django.contrib import admin
from .models import Profesor

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'especialidad', 'telefono', 'correo_electronico')
    search_fields = ('rut', 'nombre', 'apellido', 'especialidad')