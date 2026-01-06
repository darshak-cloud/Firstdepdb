from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    print("This is first view function")
    st="<h1>Welcome to our first appilcation</h1>"
    return HttpResponse(st)