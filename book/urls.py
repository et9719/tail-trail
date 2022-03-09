''' Imports '''
from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from .views import profile_list, edit_profile_list

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("book-walk/", views.AvailabilityList.as_view(), name="book-walk"),
    path("my-walks/", profile_list, name="my-walks"),
    path("edit-profile/", edit_profile_list, name="edit-profile"),
]
