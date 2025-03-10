from django.apps import AppConfig


class SparsappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sparsapp"

    def ready(self):
        import sparsapp.hooks
