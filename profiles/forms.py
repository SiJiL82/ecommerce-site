from django import forms
from crispy_forms.helper import FormHelper
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'default_phone_number',
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_county',
            'default_postcode',
            'default_country',
        ]
    first_name = forms.CharField(max_length=254)
    last_name = forms.CharField(max_length=254)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name:'
        self.fields['last_name'].label = 'Last Name'
        self.fields['default_phone_number'].label = 'Phone Number:'
        self.fields['default_street_address1'].label = 'Street Address 1:'
        self.fields['default_street_address2'].label = 'Street Address 2:'
        self.fields['default_town_or_city'].label = 'Town or City:'
        self.fields['default_county'].label = 'County:'
        self.fields['default_postcode'].label = 'Postcode:'
        self.fields['default_country'].label = 'Country:'

        self.helper = FormHelper()
        self.helper.form_show_labels = False

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
