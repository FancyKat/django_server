from django.shortcuts import render
from django.http import HttpResponse


# Request Handler

# Create your views here.

def say_hello(request):
    x=1
    y=2
    return render(request, 'hello.html', { 'name': 'Hat'})
