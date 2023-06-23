from django.contrib import admin

from .models import Carrera, Materia

# Register your models here.

class MateriaInline(admin.TabularInline):
    model = Materia
    list_display = ('nombre','duracion','carrera')
    list_filter = ('carrera',)

class CarreraAdmin(admin.ModelAdmin):
    model = Carrera
    list_display = ('nombre', 'duracion', 'institucion')
    list_editable = ('duracion',)
    list_display_links = ('nombre',)
    list_filter = ('duracion',)
    list_per_page = 3
    search_fields = ('nombre', 'duracion',)
    # readonly_fields = ('nombre',)
    inlines = [MateriaInline]




admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Materia, admin.ModelAdmin)