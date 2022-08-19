from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product
from django.conf import settings


def basket_contents(request):
    """
    Context processor to make basket information
    available on all pages
    """

    # Initialise variables
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    # Loop through each item in the session basket and add to basket_items
    for item_id, item_data in basket.items():
        # Check if it's an item with no size data
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        # Items with size data
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    # Get delivery amount from settings
    delivery = Decimal(settings.DELIVERY_AMOUNT)

    # Set grand total to order total + delivery amount
    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
