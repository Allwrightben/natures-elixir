from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    A custom widget that extends Django's ClearableFileInput for handling file
    uploads in forms, particularly useful for displaying and managing image
    uploads in the admin or front-end forms.

    It allows users to:
    - View the currently uploaded file (image or file).
    - Check a box to remove the current file (if any).
    - Upload a new file via the file input field.

    Customization:
    - `clear_checkbox_label`: Label for the checkbox used to clear/remove the
    current file.
    - `initial_text`: Label or message indicating the current file
    (shown as a link if an image).
    - `input_text`: Text next to the input box (left blank here).
    - `template_name`: Points to a custom template to render the widget.

    The widget uses Django's `gettext_lazy` for
    translation, allowing for future
    multi-language support.
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'products/custom_widget_templates/custom_clearable_file_input.html'
    )
