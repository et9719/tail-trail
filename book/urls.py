''' Imports '''
from django.urls import path, include
from . import views
from .views import profile_list, edit_profile_list

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("book-walk/", views.AvailabilityList.as_view(), name="book-walk"),
    path("my-walks/", profile_list, name="my-walks"),
    path("edit-profile/", edit_profile_list, name="edit-profile"),
]
