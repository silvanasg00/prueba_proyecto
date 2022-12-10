from django.urls import path
from proyectoG1 import views

urlpatterns = [
    path('', views.proyectoG1, name = 'proeyctoG1')
]