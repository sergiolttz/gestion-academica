from django.db import models

# Create your models here.

SEXO = [('M', 'Masculino'), ('F', 'Mujer')]

class Profesor(models.Model):
    nombre_y_apellido = models.CharField(max_length=100)
    asignatura = models.CharField(max_length=100)
    tiempo_exp = models.IntegerField()
    trayectoria_resumen = models.TextField(blank=True)  
    sexo = models.CharField(max_length=1, choices=SEXO)

    #def __str__(self):
    #    return self.nombre_y_apellido

class Estudiante(models.Model):
    nombre_y_apellido = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    promedio = models.DecimalField(max_digits=4, decimal_places=2)
    semestres_cursados = models.IntegerField()
    correo = models.EmailField()
    sexo = models.CharField(max_length=1, choices=SEXO)

    #def __str__(self):
    #   return self.nombre_y_apellido
    