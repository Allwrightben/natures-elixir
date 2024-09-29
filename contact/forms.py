from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['category', 'name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Enter your message here...'}
            ),
        }
