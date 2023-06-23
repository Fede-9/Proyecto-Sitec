from django.db.models.signals import post_save
from django.dispatch import receiver

from carreras.models import Carrera, Materia
from carreras.choices import DuracionMateria


@receiver(post_save, sender=Carrera)
def carrera_saved(sender, instance, created, **kwargs):
    if created:
        Materia.objects.create(
            nombre = 'Cursillo de ingreso',
            carrera = instance,
            duracion = DuracionMateria.MENSUAL
        )