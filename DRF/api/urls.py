from home.views import *
from django.urls import path

urlpatterns = [
    path('helloworld/', hello_world),
    path('person/', person)
]