from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. Welcome to my musicapp view")

def home(request):
    return HttpResponse("My music app home view")

