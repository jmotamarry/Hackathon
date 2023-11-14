from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):    # can use request.user
    # return HttpResponse("<h1>Hello World</h1>")   # returns a string of html
    return render(request, 'home.html', {})

def board_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'This is about us',
        'my_number': 123,
        'my_list': [1, 4, 2]

    }
    return render(request, 'board.html', my_context)