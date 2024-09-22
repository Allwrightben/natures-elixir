from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Vote
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_vote(request, product_id):
    # Get the product first
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST' and request.user.is_authenticated:
        vote_type = request.POST.get('vote_type')
        product = get_object_or_404(Product, id=product_id)

        # Determine vote value based on the vote type
        vote_value = 1 if vote_type == 'up' else -1

        # Check if the user has already voted for this product
        existing_vote = Vote.objects.filter(product=product, user=request.user).first()

        if existing_vote:
            # Update the existing vote
            existing_vote.vote = vote_value
            existing_vote.save()
        else:
            # Create a new vote
            Vote.objects.create(product=product, user=request.user, vote=vote_value)

        return redirect(reverse('product_detail', args=[product.id]))  # Redirect to the product list or the specific product page

    # If the user is not authenticated, show a message
    messages.error(request, "You need to be logged in to rate this product.")
    return redirect(reverse('product_detail', args=[product.id]))  # Redirect if not authenticated or not a POST request

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)