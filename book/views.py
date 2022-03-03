''' Imports '''
from django.shortcuts import render
from django.views import generic
from .models import Availability


class AvailabilityList(generic.ListView):
    ''' Add Docstring '''
    model = Availability
    template_name = 'book-walk.html'
    paginate_by = 14
