from .models import Category


def categories(request):
    """ Return list of categories to use globally """
    categories = Category.objects.order_by('name')
    context = {
        'categories': categories,
    }

    return context
