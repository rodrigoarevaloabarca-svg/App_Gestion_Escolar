from django.db import models

class Cursos(models.Model):
    codigo = models.CharField(max_length=100)
    nombre_curso = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codigo} - {self.nombre_curso}"



