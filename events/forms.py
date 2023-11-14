from django import forms


from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'posting_club',
        ]



class RawEventForm(forms.Form):
    title           = forms.CharField()
    description     = forms.CharField()
    posting_club    = forms.CharField()