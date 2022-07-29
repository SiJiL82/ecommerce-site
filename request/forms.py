from django import forms
from .models import Request


class NewRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = (
            'name',
            'category',
            'size',
            'description',
        )
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4
            })
        }

    def __init__(self, *args, **kwargs):
        super(NewRequestForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Full Name:'
        self.fields['category'].label = 'Category:'
        self.fields['size'].label = 'Size:'
        self.fields['description'].label = 'Description:'
