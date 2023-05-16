from django.contrib import admin

from .models import Carrera, Materia

# Register your models here.
class CarreraAdmin(admin.ModelAdmin):
    model = Carrera
    list_display = ('nombre', 'duracion', 'institucion')

    def institucion(self, obj:Carrera):
        return "Itec"
    

class MateriaAdmin(admin.ModelAdmin):
    model = Materia
    list_display = ('nombre', 'duracion', 'carrera')
    


admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Materia, MateriaAdmin)