from django.apps import AppConfig


class WishlistConfig(AppConfig):
    """
    Configuration for the Wishlist application.

    This class defines the configuration for the
    Wishlist app within the Django project.
    It includes the default auto field type and the name of the app.

    Attributes:
        default_auto_field: The default field type for
        auto-generated fields in the app.
        name: The name of the application
        as it appears in the project's settings.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wishlist'
