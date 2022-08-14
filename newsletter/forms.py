from django import forms
from .models import Newsletter
from crispy_forms.helper import FormHelper


class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = (
            'full_name',
            'email',
        )

    def __init__(self, *args, **kwargs):
        super(NewsletterSignupForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = 'Full Name:'
        self.fields['email'].label = 'Email Address:'

        self.helper = FormHelper()
        self.helper.form_show_labels = False

        self.fields['full_name'].widget.attrs['autofocus'] = True
