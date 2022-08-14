from django.contrib import admin
from .models import Category, Product, Review
from .forms import ProductsAdminForm


class CategoryAdmin(admin.ModelAdmin):
    """Categories admin screen config"""
    list_display = (
        'friendly_name',
        'name',
        'plural_name'
    )


admin.site.register(Category, CategoryAdmin)


class ProductsAdmin(admin.ModelAdmin):
    """ Products admin screen config """

    list_display = (
            'sku',
            'friendly_name',
            'category',
            'price',
        )
    ordering = ('sku',)
    form = ProductsAdminForm


admin.site.register(Product, ProductsAdmin)


class ReviewsAdmin(admin.ModelAdmin):
    """ Reviews admin screen config """
    list_display = (
        'name',
        'product',
        'rating',
        'date',
    )
    ordering = ('date',)


admin.site.register(Review, ReviewsAdmin)
