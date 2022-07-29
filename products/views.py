from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.db.models.functions import Lower
from django.db.models import Q
from products.forms import NewReviewForm
from .models import Product, Category, Review


def all_products(request):
    """ A view to show all products, including sorting and filtering """
    products = Product.objects.all()
    query = None
    selected_category = None
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
            category = request.GET['category']
            products = products.filter(category__name__in=(category,))
            selected_category = Category.objects.filter(
                name__in=(category, ))[0]

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_category': selected_category,
        'current_sorting': current_sorting
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show product details for a single product """
    product = get_object_or_404(Product, pk=product_id)

    product_reviews = Review.objects.filter(product=product_id)

    if request.method == 'POST':
        new_review_form = NewReviewForm(data=request.POST)
        if new_review_form.is_valid():
            review_form = new_review_form.save(commit=False)
            review_form.user_id = request.user
            review_form.product = product
            review_form.save()

    context = {
        'product': product,
        'reviews': product_reviews,
        'new_review_form': NewReviewForm()
    }

    return render(request, 'products/product_details.html', context)
