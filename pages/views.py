from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home_view(request, *args, **kwargs):    # can use request.user
    # return HttpResponse("<h1>Hello World</h1>")   # returns a string of html
    return render(request, 'home.html', {})

def create_user_view(request):
    if request.method == 'POST':
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print(request.POST.get)
        User.objects.create_user(username=request.POST.get('inputEmail3'), password=request.POST.get('inputPassword3'))
    return render(request, 'create_user.html', {})