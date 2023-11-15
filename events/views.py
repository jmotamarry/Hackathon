from django.shortcuts import render, get_object_or_404, redirect

from .forms import EventForm, RawEventForm
from .models import Event

# Create your views here.
def event_delete_view(request, id):
    obj = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        obj.delete()                        # confirm the user wants to delete the object
        return redirect('/board/')
    context = {
        'object': obj,
    }
    return render(request, 'events/event_delete.html', context)

def event_detail_view(request, id):         # shows one event
    obj = get_object_or_404(Event, id=id)   # get object id=id, if it does not exist throw 404 error
    if obj.approved == True:
        context = {                             # defines what to pass in to event_detail.html
            'object': obj,
        }
        return render(request, 'events/event_detail.html', context)
    else:
        return render("<h1>This event has not been approved</h1>")

def event_board_view(request, *args, **kwargs):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'events/event_board.html', context)

def event_create_view(request):                                         # not working to authenticate user
    if request.user != 'AnonymousUser':                                 # tries to prevent someone not logged in from making an event
        form = EventForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/board/')                                  # redirect to board if the form is saved

        context = {
            'form': form
        }
        return render(request, 'events/event_create.html', context)
    else:
        return render("<h1>You are not logged in</h1>", {})

