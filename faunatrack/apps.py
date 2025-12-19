from django.apps import AppConfig


class FaunatrackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'faunatrack'

    def ready(self):
        import faunatrack.signals  # noqa: F401