from django.core.paginator import Paginator
from django.shortcuts import  HttpResponse, render

from .forms import CarreraForm
from .repository import CarreraRepository



def index(request):
    return render(
        request,
        'carreras/inicio.html'
    )


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
    
    # Creamos la instancia del paginador,
    # y le pasamos como parametro el listado y la cantidad por pagina
    paginator = Paginator(carreras, 4)
    # Obtenemos de la peticion la pagina que queremos mostrar URL?pagina=5
    page = request.GET.get('pagina')
    # Generamos un objeto paginado, que retorna el modelo y el numero de paginas
    page_obj = paginator.get_page(page)

    return render(
        request, 
        'carreras/index_carreras.html',
        {
            'form': carrera_form,
            'carreras': carreras,
            'ok':ok,
            'page_obj': page_obj
        }
    )
       


def materias_view(request):
    return HttpResponse('Esta es la web de Materias')

