from django import forms

from admin import User

class EventForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
           # 'email',   =
           # 'password' = 
           # 'remember' = 
        ]
