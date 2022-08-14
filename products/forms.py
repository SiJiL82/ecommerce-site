from django import forms
from .models import Review, Product
from .widgets import CustomClearableFileInput


class NewReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'name',
            'rating',
            'review',
        )
        widgets = {
            'review': forms.Textarea(attrs={
                'rows': 4
            })
        }

    def __init__(self, *args, **kwargs):
        super(NewReviewForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Full Name:'
        self.fields['rating'].label = 'Rating:'
        self.fields['review'].label = 'Review:'


class ProductsAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        widgets = {
            'image': CustomClearableFileInput
        }
        fields = (
            'sku',
            'friendly_name',
            'category',
            'description',
            'price',
            'image',
            'sizes',
            'ready_to_ship',
        )
