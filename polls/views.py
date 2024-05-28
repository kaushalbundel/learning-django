from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# this is a function based view(FBV), there is also a class based view(CBV)
def index(request):
    return HttpResponse("Hello World! You are at polls index.")
