''' Imports '''
from django.urls import path
from . import views


urlpatterns = [
    path("",  views.AvailabilityList.as_view(), name="home"),
]
