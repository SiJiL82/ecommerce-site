from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def read_verification_file(request):
    file = open(settings.STATIC_URL + 'google8ed90ed434c84dc3.html')
    file_content = file.read()
    file.close()
    return HttpResponse(file_content, content_type="text/plain")
