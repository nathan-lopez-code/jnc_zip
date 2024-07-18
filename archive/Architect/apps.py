from django.apps import AppConfig


class ArchitectAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Architect'

    def ready(self):
        import Architect.models  # Ensure models are loaded and signals are connected