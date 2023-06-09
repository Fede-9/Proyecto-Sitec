from django.contrib import admin

from patrones.models import CovidInfo


# Register your models here.

@admin.register(CovidInfo)
class CovidInfoAdmin(admin.ModelAdmin):
    model = CovidInfo
    list_display = ('date', 'positive', 'negative', 'diferencia')

    def diferencia(self, instance):
        return instance.diff
