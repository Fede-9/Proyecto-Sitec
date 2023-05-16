import factory

from .models import Carrera

class CarreraFactory(factory.Factory):
    class Meta:
        model = Carrera
        
    nombre = 'Educacion Fisica'
    duracion = 2

