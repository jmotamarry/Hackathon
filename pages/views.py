from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

# Create your views here.
def home_view(request, *args, **kwargs):    # can use request.user
    # return HttpResponse("<h1>Hello World</h1>")   # returns a string of html
    return render(request, 'home.html', {})