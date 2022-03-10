''' Imports '''
from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from .views import profile_list, ProfileCreateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("book-walk/", views.AvailabilityList.as_view(), name="book-walk"),
    path("my-walks/", profile_list, name="my-walks"),
    path("profile_create_form.html", views.ProfileCreateView.as_view(template_name="profile_create_form.html"), name="create_form"),
    # path("edit-profile/", edit_profile_list, name="edit-profile"),
]
