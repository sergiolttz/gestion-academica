from django.shortcuts import render
from .models import Estudiante, Profesor
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def pagina_formulario(request):
    return render(request, 'form.html')

def busqueda_profesor(request):
    if request.GET.get('profesor'):
        nombre_solicitado = request.GET['profesor']
        lista_personas = Profesor.objects.filter(nombre_y_apellido__icontains=nombre_solicitado)
        return render(request, 'resultados.html', {'busqueda': nombre_solicitado, 'personas': lista_personas, 'tipo': 'profesor'})
    else:
        return HttpResponse('búsqueda vacía')

def busqueda_estudiante(request):
    if request.GET.get('estudiante'):
        nombre_solicitado = request.GET['estudiante']
        lista_personas = Estudiante.objects.filter(nombre_y_apellido__icontains=nombre_solicitado)
        return render(request, 'resultados.html', {'busqueda': nombre_solicitado, 'personas': lista_personas, 'tipo': 'estudiante'})
    else:
        return HttpResponse('búsqueda vacía')