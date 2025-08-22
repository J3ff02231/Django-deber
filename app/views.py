from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, World!")
def nombre(request):
    return HttpResponse("Mi nombre: Jefferson Recalde")
def hola(request):
    return HttpResponse("Hola mundo")
def hello(request):
    return HttpResponse("Hello from hello view!")