from django.shortcuts import render

from .models import Event

# Create your views here.

def event_detail_view(request):     # shows one event
    obj = Event.objects.get(id=1)
    context = {
        'object': obj,
    }

    return render(request, 'events/event_detail.html', context)