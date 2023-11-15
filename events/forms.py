from django import forms
from django.forms.widgets import DateTimeInput

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'repeats',
            'start_time',
            'end_time',
            'posting_club',
        ]
        widgets = {
            'start_time': DateTimeInput(attrs={'type': 'date'}),
            'end_time': DateTimeInput(attrs={'type': 'date'}),
        }
