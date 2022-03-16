''' Imports '''
from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import profile_list, profile_create, profile_update

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("book-walk/", views.AvailabilityList.as_view(), name="book-walk"),
    path("my-walks/", profile_list, name="my-walks"),
    path("profile-create/", profile_create, name="profile-create"),
    path("profile-update/", profile_update, name="profile-update"),
]
