
from django.urls import path
from .views import time_wold

urlpatterns = [
    path('',time_wold,name="time_world")
]
