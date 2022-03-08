''' Imports '''
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("book-walk.html", views.AvailabilityList.as_view(), name="book-walk"),
    path("my-walks.html", views.ProfileList.as_view(), name="my-walks"),
]
