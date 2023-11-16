from django import forms
from django.forms.widgets import TimeInput, DateInput

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'repeats',
            'date',
            'start_time',
            'end_time',
            'posting_club',
        ]
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'start_time': TimeInput(attrs={'type': 'time'}),
            'end_time': TimeInput(attrs={'type': 'time'}),
        }