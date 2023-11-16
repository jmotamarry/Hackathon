from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import EventForm
from .models import Event

# Create your views here.
def event_delete_view(request, id):
    obj = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        obj.delete()                        # confirm the user wants to delete the object
        return redirect('/event/board/')
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
        return HttpResponse("<h1>This event has not been approved</h1>")

def event_board_view(request, *args, **kwargs):                 # passes the sorted list of all the objects and prints them in order
    print(request.user.get_all_permissions())
    sorted_list = Event.objects.all().order_by('date', 'start_time')
    context = {
        'object_list': sorted_list
    }
    return render(request, 'events/event_board.html', context)


def event_update_view(request, id=id):
    obj = get_object_or_404(Event, id=id)
    form = EventForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/event/board/')
    context = {
        'object': obj,
        'form': form,
    }
    return render(request, 'events/event_update.html', context)


def event_create_view(request):                                         # not working to authenticate user
    form = EventForm(request.POST or None)
    if form.is_valid():
        event = form.save(commit=False)
        event.user = request.user
        event.save()

        return redirect('/event/board/')                                  # redirect to board if the form is saved

    context = {
        'form': form
    }
    return render(request, 'events/event_create.html', context)