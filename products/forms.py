from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Form for creating and updating Product instances.

    This form allows users to manage product details, including an optional
    image upload using a custom clearable file input widget, and dynamically
    sets category choices based on available categories in the database.
    """

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        """
        Initialize the ProductForm, dynamically setting category choices
        with friendly names and applying custom CSS classes to form fields.
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-green'
