from django import forms
from crispy_forms.helper import FormHelper
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'street_address1',
            'street_address2',
            'town_or_city',
            'postcode',
            'county',
            'country',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        self.fields['full_name'].label = 'Full Name:'
        self.fields['email'].label = 'Email Address:'
        self.fields['phone_number'].label = 'Phone Number:'
        self.fields['country'].label = 'Country:'
        self.fields['postcode'].label = 'Postcode:'
        self.fields['town_or_city'].label = 'Town or City:'
        self.fields['street_address1'].label = 'Street Address 1:'
        self.fields['street_address2'].label = 'Street Address 2:'
        self.fields['county'].label = 'County:'
        # self.fields['country'].disabled = True

        self.helper = FormHelper()
        self.helper.form_show_labels = False

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
