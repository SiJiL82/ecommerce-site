from django import forms
from .models import Review


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
