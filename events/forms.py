from django import forms
from .models import Event


class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'location_name',
            'location_address',
            'date',
            'start_time',
            'end_time',
            'description',
            'google_maps_link',
        )
    widgets = {
        'date': forms.DateInput(attrs={
            'type': 'date',
        }),
        'location_address': forms.Textarea(attrs={
            'rows': 4
        }),
        'description': forms.Textarea(attrs={
            'rows': 2
        })
    }

    def __init__(self, *args, **kwargs):
        super(NewEventForm, self).__init__(*args, **kwargs)
        self.fields['location_name'].label = 'Location:'
        self.fields['location_address'].label = 'Address:'
        self.fields['date'].label = 'Date:'
        self.fields['start_time'].label = 'Start time:'
        self.fields['end_time'].label = 'End time:'
        self.fields['description'].label = 'Description:'
        self.fields['google_maps_link'].label = 'Map Link:'
