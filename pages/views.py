from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):    # can use request.user
    return HttpResponse("<h1>Hello World</h1>")

def event_view(request, *args, **kwargs):
    return HttpResponse("<h1>Event Page</h1>")