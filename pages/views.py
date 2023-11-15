from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from pages.forms import UserForm

# Create your views here.
def home_view(request, *args, **kwargs):    # can use request.user
    # return HttpResponse("<h1>Hello World</h1>")   # returns a string of html
    return render(request, 'home.html', {})

def create_user_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/event/board/')                                  # redirect to board if the form is saved
    context = {
        'form': form
    }
    return render(request, 'events/event_create.html', context)