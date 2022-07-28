from django.contrib import admin
from .models import Request

class RequestAdmin(admin.ModelAdmin):
    """ Requests admin screen config """
    list_display = (
        'name',
        'date_created',
        'fulfilled',
    )
admin.site.register(Request, RequestAdmin)
