from django.shortcuts import  HttpResponse, render
from .forms import CarreraForm

from .repository import CarreraRepository



def index(request):
    return HttpResponse('Este es el Index')


def carrera_view(request, ok: bool=False):
    carrera_form = CarreraForm
    repository = CarreraRepository()
    carreras = repository.get_all_carreras()

    if request.method == 'POST':
        carrera_form = carrera_form(data=request.POST)
        if carrera_form.is_valid():
            nombre = request.POST.get('nombre')
            duracion = request.POST.get('duracion')
            repository.create_carrera(
                nombre=nombre,
                duracion=duracion
            )
            ok=True

    return render(
        request, 
        'carreras/index_carreras.html',
        {
            'form': carrera_form,
            'carreras': carreras,
            'ok':ok
        }
    )
       


def materias_view(request):
    return HttpResponse('Esta es la web de Materias')

