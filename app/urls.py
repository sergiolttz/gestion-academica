from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.index, name='index'),  # Example: maps the root path to the 'index' view
    path('formulario/', views.pagina_formulario, name='pagina_formulario'),  # Example: maps the 'formulario' path to the 'pagina_formulario' view
    path('busqueda_profesor/', views.busqueda_profesor, name='busqueda_profesor'),  # Example: maps the 'busqueda_profesor' path to the 'busqueda_profesor' view    
    path('busqueda_estudiante/', views.busqueda_estudiante, name='busqueda_estudiante'),  # Example: maps the 'busqueda_estudiante' path to the 'busqueda_estudiante' view
]