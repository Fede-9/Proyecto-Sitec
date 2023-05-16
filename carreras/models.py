from django.db import models
from enumchoicefield import EnumChoiceField

from .choices import DuracionMateria

# Create your models here.
class Carrera(models.Model):

    DURACION = (
        (1, "UNO"),
        (2, "DOS"),
        (3, "TRES"),
    )
    nombre = models.CharField(
        verbose_name='Carrera',
        max_length=100,
    )
    duracion = models.IntegerField(
        verbose_name="Duracion",
        choices=DURACION,
    )
    created_at = models.DateTimeField(
        verbose_name='Creado el',
        auto_now=True,
        )
    update_at = models.DateTimeField(
        verbose_name='Actualizado el',
        auto_now_add=True,
        )
    
    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"

    def __str__(self) -> str:
        return self.nombre
    

class Materia(models.Model):
    nombre = models.CharField(
        verbose_name='Materia',
        max_length=100,
    )
    carrera = models.ForeignKey(
        Carrera,
        verbose_name= 'Carrera',
        on_delete=models.CASCADE,
    )
    duracion = EnumChoiceField(
        DuracionMateria,
        default=DuracionMateria.SEMESTRAL
    )

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        unique_together = ['nombre', 'carrera']

    def get_nombre_y_duracion(self):
        return f"La materia {self.nombre} dura {self.duracion.value}"
