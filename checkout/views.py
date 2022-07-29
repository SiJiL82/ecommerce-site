from django.shortcuts import render, redirect, reverse
from .forms import OrderForm
from django.conf import settings


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
