from django import forms
from django.forms.widgets import TimeInput, DateInput

from .models import Event


class EventForm(forms.ModelForm):       # main form for our project, each event form has these attributes
    class Meta:
        model = Event
        fields = [                      # these are the attributes on the form
            'title',
            'description',
            'repeats',
            'date',
            'start_time',
            'end_time',
            'posting_club',
            'image',
        ]
        widgets = {                     # sets the type on the form
            'date': DateInput(attrs={'type': 'date'}),
            'start_time': TimeInput(attrs={'type': 'time'}),
            'end_time': TimeInput(attrs={'type': 'time'}),
        }