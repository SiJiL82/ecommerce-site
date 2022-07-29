from django.shortcuts import render
from django.conf import settings


def faqs(request):
    """ A view to return the FAQ page """

    context = {
        'delivery_amount': settings.DELIVERY_AMOUNT
    }

    return render(request, 'faqs/faqs.html', context)
