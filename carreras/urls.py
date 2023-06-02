from django.urls import path

from .views import carrera_view, materias_view


urlpatterns = [
    path('', carrera_view, name='carreras'),
    path('materias/', materias_view, name='materias'),
]