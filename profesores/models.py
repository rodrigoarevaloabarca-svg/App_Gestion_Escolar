from django.db import models

class Profesor(models.Model):
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo_electronico = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.rut}"