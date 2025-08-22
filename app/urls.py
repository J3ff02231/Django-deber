from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('nombre/', views.nombre, name='nombre'),
    path('hola/', views.hola, name='hola'),
]
