from django.db import models
from django.contrib.auth.models import User
import uuid

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)  # Ensure SKU is unique
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.sku:
            # Generate a unique SKU when saving the product
            self.sku = str(uuid.uuid4())[:12].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    # Method to count thumbs up votes
    def thumbs_up_count(self):
        return self.votes.filter(vote=Vote.THUMBS_UP).count()

    # Method to count thumbs down votes
    def thumbs_down_count(self):
        return self.votes.filter(vote=Vote.THUMBS_DOWN).count()


class Vote(models.Model):
    THUMBS_UP = 1
    THUMBS_DOWN = -1
    VOTE_CHOICES = [
        (THUMBS_UP, 'Thumbs Up'),
        (THUMBS_DOWN, 'Thumbs Down'),
    ]

    product = models.ForeignKey(Product, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)
    vote = models.SmallIntegerField(choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('product', 'user')  # Ensure one vote per product per user

    def __str__(self):
        return f"{self.user.username} - {self.get_vote_display()} on {self.product.name}"