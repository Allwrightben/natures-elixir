from django.db import models


class Contact(models.Model):
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
