from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist, WishlistItem
from products.models import Product
from django.db import IntegrityError


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    try:
        WishlistItem.objects.create(wishlist=wishlist, product=product)
        messages.success(request, f"{product.name} added to your wishlist.")
    except IntegrityError:
        messages.info(request, f"{product.name} is already in your wishlist.")

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def view_wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    items = WishlistItem.objects.filter(wishlist=wishlist)
    return render(request, 'wishlist/wishlist.html', {'items': items})


@login_required
def move_to_bag(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    try:
        # Find the item in the wishlist and remove it
        item = WishlistItem.objects.get(wishlist=wishlist, product=product)
        item.delete()

        # Add the product to the shopping bag
        quantity = 1
        bag = request.session.get('bag', {})

        if product_id in bag:
            bag[product_id] += quantity
        else:
            bag[product_id] = quantity

        request.session['bag'] = bag

        messages.success(
            request,
            f"{product.name} successfully moved to your shopping bag."
        )
    except WishlistItem.DoesNotExist:
        messages.error(request, f"{product.name} is not in your wishlist.")

    return redirect('wishlist:view_wishlist')


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    try:
        # Find the item in the wishlist and remove it
        item = WishlistItem.objects.get(wishlist=wishlist, product=product)
        item.delete()
        messages.success(request, f"{product.name} has been removed from your wishlist.")
    except WishlistItem.DoesNotExist:
        messages.error(request, f"{product.name} is not in your wishlist.")

    return redirect('wishlist:view_wishlist')
