''' Imports '''
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Availability, Profile


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    ''' What admin will be able to do/see '''
    list_display = ('date', 'time')
    list_filter = ('date', 'time')
    search_fields = ['date']


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    ''' A list of whats deisplayed, what can be filtered
    and how you can search for things on the admin page for
    a profile '''
    list_display = ('owner', 'dog', 'phonenumber')
    list_filter = ('owner', 'dog')
    search_fields = ['owner', 'dog']
    summernote_fields = ('info')
