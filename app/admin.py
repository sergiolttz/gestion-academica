from django.contrib import admin
from .models import Profesor, Estudiante
# Register your models here.

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display=['nombre_y_apellido']

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display=['nombre_y_apellido', 'semestres_cursados']