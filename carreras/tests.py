import pytest

from .models import Carrera
from .repository import CarreraRepository
from .factories import CarreraFactory

# Create your tests here.

def test_comapre_parameters():
    a = 10
    b = 15
    c = a + b 

    assert c == 25


# este decorador es para que lo teste pero no afecte a la base de datos
@pytest.mark.django_db
def test_get_carreras():
    carrera_nueva = Carrera.objects.create(
        nombre = 'Tecnico superior Electromecanica',
        duracion = 2,
    )

    repository = CarreraRepository()
    carreras = repository.get_all_carreras()

    assert carreras.count() == 1
    assert carreras[0].nombre == carrera_nueva.nombre


@pytest.mark.django_db
def test_create_carrera():
    nombre = 'Medicina'
    anios = 2

    repository = CarreraRepository()
    carrera = repository.create_carrera(
        nombre,
        anios
    )

    assert carrera.nombre == 'nombre'


@pytest.mark.django_db
def test_get_carreras():
    for x in range(10):
        carrera = CarreraFactory()
        carrera.save()

    repository = CarreraRepository()
    carreras = repository.get_all_carreras()

    assert carreras.count() == 1
    assert carreras[0].nombre == carrera.nombre