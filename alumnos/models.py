from django.db import models
from django.db import models

class Alumno(models.Model):
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.rut}"



