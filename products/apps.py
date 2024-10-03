from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    Configuration class for the 'products' app.

    Specifies the default type for auto-generated fields and sets the
    application name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
