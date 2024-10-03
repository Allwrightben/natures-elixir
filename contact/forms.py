from django import forms
from .models import Contact

"""
Forms for the Contact app.

This module contains the form for
 users to submit inquiries through the Contact model.
"""


class ContactForm(forms.ModelForm):
    """
    A form for submitting contact inquiries.

    This form uses the Contact model and includes fields for
    category, name,  email, and a message. The message field
    uses a Textarea widget for improved usability.

    Attributes:
        Meta (class): Defines the model to use
        and the fields to include in the form.
    """
    class Meta:
        model = Contact
        fields = ['category', 'name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Enter your message here...'}
            ),
        }
