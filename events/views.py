from django.shortcuts import render

from .forms import EventForm, RawEventForm
from .models import Event

# Create your views here.

def event_create_view(request):
    form = RawEventForm()
    context = {
        "form": form
    }
    return render(request, 'events/event_create.html', context)

"""
def event_create_view(request):
    title = request.POST.get('title')   # gets the data safely, using POST
    print(title)
    context = {}
    return render(request, 'events/event_create.html', context)


def event_create_view(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EventForm()

    context = {
        'form': form
    }
    return render(request, 'events/event_create.html', context)
"""


def event_detail_view(request):     # shows one event
    obj = Event.objects.get(id=1)   # get object 1
    context = {                     # defines what to pass in to event_detail.html
        'object': obj,
    }
    return render(request, 'events/event_detail.html', context)