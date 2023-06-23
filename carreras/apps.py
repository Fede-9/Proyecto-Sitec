from django.apps import AppConfig


class CarrerasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carreras'


    def ready(self) -> None:
        import carreras.signals
