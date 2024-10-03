from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration class for the 'home' app.

    This class sets the default auto field to BigAutoField and defines
    the app's name as 'home'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
