from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    """ Event admin screen config """
    list_display = (
        'location_name',
        'date',
    )
admin.site.register(Event, EventAdmin)
