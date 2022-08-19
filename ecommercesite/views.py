from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


# TODO: Replace these 3 calls with a single view for any static file
def read_verification_file(request):
    file = open(settings.STATICFILES_DIRS[0] + '/google8ed90ed434c84dc3.html')
    file_content = file.read()
    file.close()
    return HttpResponse(file_content, content_type="text/plain")


def read_sitemap(request):
    file = open(settings.STATICFILES_DIRS[0] + '/sitemap.xml')
    file_content = file.read()
    file.close()
    return HttpResponse(file_content, content_type="text/plain")


def read_robots(request):
    file = open(settings.STATICFILES_DIRS[0] + '/robots.txt')
    file_content = file.read()
    file.close()
    return HttpResponse(file_content, content_type="text/plain")
