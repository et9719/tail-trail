''' Imports '''
from django.shortcuts import render
from django.views import generic
from .models import Availability, Profile


class Home(generic.ListView):
    ''' what model we want to see, where we want to see it
    and the max number of times we want to see it on one page '''
    model = Availability
    template_name = 'index.html'
    paginate_by = 1


class ProfileList(generic.ListView):
    ''' what model we want to see, where we want to see it
    and the max number of times we want to see it on one page '''
    model = Profile
    template_name = 'my-walks.html'
    paginate_by = 1


def profile_list(request):
    ''' what model we want to see, where we want to see it '''
    profile = Profile.objects.filter(
        user=request.user.id
    ).first()
    context = {
        "profile": profile if profile else None
    }
    return render(request, "my-walks.html", context)

def edit_profile_list(request):
    ''' what model we want to see, where we want to see it '''
    profile = Profile.objects.filter(
        user=request.user.id
    ).first()
    context = {
        "profile": profile if profile else None
    }
    return render(request, "edit-profile.html", context)

class AvailabilityList(generic.ListView):
    ''' what model we want to see, where we want to see it
    and the max number of times we want to see it on one page '''
    model = Availability
    template_name = 'book-walk.html'
    paginate_by = 14
