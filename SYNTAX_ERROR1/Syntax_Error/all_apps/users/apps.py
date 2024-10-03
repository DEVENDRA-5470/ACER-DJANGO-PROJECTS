from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'all_apps.users'

    def ready(self):
        # Import signals when the app is ready
        import all_apps.users.signals