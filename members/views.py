from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from events.models import Event

# Create your views here.
def login_user(request):        # directs a user to a form to log in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have successfully logged in"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in, Try again"))
            return redirect('/members/login_user/')


    else:
        return render(request, 'authenticate/login.html', {})
    
def logout_user(request):           # logs out a user
    logout(request)
    messages.success(request, ("Logged Out Successfully"))
    return redirect('/event/board/')

def register_user(request):         # directs a user to a form to create account
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Account creation successful"))
            return redirect("/event/board/")
    else:
        form = UserCreationForm()
    return render(request, 'authenticate/register_user.html', {'form': form})

def moderator_view(request):        # directs to a page for only moderators
    sorted_list = Event.objects.all().order_by('date', 'start_time')
    return render(request, 'authenticate/moderator.html', { 'object_list': sorted_list })

def moderator_event_detail_view(request, id):           # shows one event
    obj = get_object_or_404(Event, id=id)               # get object id=id, if it does not exist throw 404 error
    context = {                                         # defines what to pass in to event_detail.html
        'object': obj,
    }
    return render(request, 'authenticate/moderator_event_detail.html', context)
    
def moderator_update_view(request, id=id):      # lets a moderator approve an object
    obj = get_object_or_404(Event, id=id)
    obj.approved = True
    obj.save(update_fields=['approved'])
    messages.success(request, ("Event Approved"))
    return redirect('/members/moderator/')

def moderator_delete_view(request, id=id):
    obj = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        obj.delete()                        # confirm the user wants to delete the object
        return redirect('/members/moderator/')
    context = {
        'object': obj,
    }
    return render(request, 'authenticate/moderator_delete.html', context)