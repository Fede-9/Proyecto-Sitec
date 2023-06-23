lista_de_niveles = [
    'Grado',
    'Postgrado',
    'Terciario',
    'Diplomatura'
]

def niveles(request):
    return {'niveles': lista_de_niveles}