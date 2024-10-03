from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    """
    Model representing a user's wishlist.

    Attributes:
        user: A foreign key linking to the User who owns the wishlist.
        products: A many-to-many relationship linking
        to the Product model through WishlistItem.
        created_at: The date and time when the wishlist was created.
        modified_at: The date and time when the wishlist was last modified.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='WishlistItem')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s wishlist"


class WishlistItem(models.Model):
    """
    Model representing an item in a wishlist.

    Attributes:
        wishlist: A foreign key linking to the Wishlist
        that contains this item.
        product: A foreign key linking to the Product that is in the wishlist.
        added_at: The date and time when the product was added to the wishlist.
    """
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('wishlist', 'product')

    def __str__(self):
        return (
            f"{self.product.name} in "
            f"{self.wishlist.user.username}'s wishlist"
        )
