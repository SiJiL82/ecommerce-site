from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    """Categories admin screen config"""
    list_display = (
        'friendly_name',
        'name',
    )
admin.site.register(Category, CategoryAdmin)