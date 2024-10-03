from django.db import models

"""
Models for the Contact app.

This module contains the Contact model, which stores information submitted by
users through a contact form, including the category of inquiry, the user's
name, email, and message.
"""


class Contact(models.Model):
    """
    A model representing a contact inquiry.

    Attributes:
        category (str): The category of the inquiry, such as 'products' or
        'collaboration'. name (str): The name of the person making the inquiry.
        email (str): The email address of the person making the inquiry.
        message (str): The message content of the inquiry, up to 1000
        characters.
    """
    CATEGORY_CHOICES = [
        ('products', 'Products'),
        ('collaboration', 'Collaboration'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    message = models.TextField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return f"{self.category}: {self.message[:30]}..."
