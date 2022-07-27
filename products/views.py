from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Product, Category

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
                products  = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category']
            print(category)
            products = products.filter(category__name__in=(category,))
            print(products)
            selected_category = Category.objects.filter(name__in=(category, ))[0]

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_category': selected_category,
        'current_sorting': current_sorting
    }

    return render(request, 'products/products.html', context)