''' Imports '''
from django.contrib import admin
from .models import Availability


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    ''' What admin will be able to do/see '''
    list_display = ('date', 'time')
    list_filter = ('date', 'time')
    search_fields = ['date']
