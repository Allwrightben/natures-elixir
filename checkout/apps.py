from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configuration for the Checkout app.

    This class defines the configuration for the Checkout application,
    including the default auto field type and the app's name. It also
    imports signals when the app is ready.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals  # noqa
