from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.utils.safestring import mark_safe


def view_basket(request):
    """ A view that renders the basket contents page """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the basket """

    # Init variables
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    size = None

    # Check if basket item has a size and set if applicable
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # If size is set, add to a unique key so duplicate items
    # of different sizes aren't combined
    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
            else:
                basket[item_id]['items_by_size'][size] = quantity
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    # Set the session basket to the updated basket object
    request.session['basket'] = basket

    # Show success message to user
    message = """
        Item added to
        <a href='{url}' class='text-brand'>
            <strong>basket</strong>
        </a>!
    """
    basket_url = reverse("view_basket")
    messages.success(
        request,
        mark_safe(message.format(url=basket_url))
    )

    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust quantity of the specified product to the specified amount """

    # Init variables
    quantity = int(request.POST.get('quantity'))
    size = None

    # Check if product has size property
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    # If size is set, make sure we adjust the correct basket item
    if size:
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
        else:
            del basket[item_id]['items_by_size'][size]
        if not basket[item_id]['items_by_size']:
            basket.pop(item_id)
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(item_id)

    # Update the session basket to the basket object
    request.session['basket'] = basket

    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove the item from the shopping basket """

    try:
        # Init variables
        size = None

        # Check if item has size property
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        # If size is set, make sure we remove the correct item from the basket.
        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
        else:
            basket.pop(item_id)

        # Update the session basket to the basket object
        request.session['basket'] = basket

        # Show success message to the user
        messages.success(
            request,
            'Item removed from basket'
        )

        return HttpResponse(status=200)
    except Exception:
        # Return an error as product can't be removed from the basket.
        # TODO: This should really invalidate the user's whole basket
        # as something has gone very wrong
        return HttpResponse(status=500)
