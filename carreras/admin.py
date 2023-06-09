from django.contrib import admin

from .models import Carrera, Materia

# Register your models here.
class CarreraAdmin(admin.ModelAdmin):
    model = Carrera
    list_display = ('nombre', 'duracion', 'institucion')
    list_editable = ('duracion',)
    list_display_links = ('nombre',)
    list_filter = ('duracion',)
    list_per_page = 3
    search_fields = ('nombre', 'duracion',)
    readonly_fields = ('nombre',)


class MateriaAdmin(admin.ModelAdmin):
    model = Materia
    list_display = ('nombre', 'duracion', 'carrera')
    


admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Materia, MateriaAdmin)