from django.shortcuts import render
from .models import Estudiante, Profesor
from django.http import HttpResponse

def index(request):  
    return render(request, 'index.html')

def pagina_formulario(request):
    return render(request, 'form.html')

def busqueda_profesor(request):
    
    if request.GET['profesor']:
        
        nombre_solicitado = request.GET ['profesor']

        try:
            profesor = Profesor.objects.get(nombre_y_apellido = nombre_solicitado)
        except Exception as ex:
            mensaje = f'Ocurrió un error: {ex}'
        else:
            mensaje = f'Años de experiencia {profesor.tiempo_exp} <br> Asignatura: {profesor.Asignaura}'
        finally:
            return HttpResponse('<h1>'+mensaje+'</h1>')
    
    else:
        return HttpResponse('Busqueda vacia')
    
lista_estudiantes = Estudiante.objects.all()

def busqueda_estudiante(request):
    if request.GET['estudiante']:
        nombre_solicitado = request.GET['estudiante']

        lista_personas = Estudiante.objects.filter(nombre_y_apellido__icontains = nombre_solicitado)

        ...

        lista_personas = []
        for i in lista_estudiantes:
            if i.nombre_y_apellido == nombre_solicitado:
                lista_personas.append(i)
        ...

        return render(request, 'resultados.html', {'busqueda': nombre_solicitado, 'personas': lista_personas})
    else:
        return HttpResponse('busqueda vacia')


# Create your views here.
