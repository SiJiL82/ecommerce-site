from django.shortcuts import render


def faqs(request):
    """ A view to return the FAQ page """
    return render(request, 'faqs/faqs.html')
