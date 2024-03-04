from django.shortcuts import render
from django.views import generic
from .models import Schedule

# Create your views here.
class ScheduleList(generic.ListView):
    model = Schedule


