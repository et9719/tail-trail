''' Imports '''
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Availability, Profile
# from .forms import ProfileForm


# class ProfileList(generic.ListView):
#     ''' what model we want to see, where we want to see it
#     and the max number of times we want to see it on one page '''
#     model = Profile
#     template_name = 'my-walks.html'
#     paginate_by = 1


# def edit_profile_list(request):
#     ''' what model we want to see, where we want to see it '''
#     return render(
#         request,
#         "edit-profile.html",
#         {
#             "profile_form": ProfileForm()
#         },
#     )

# class ProfileList(CreateView):
#     model = Profile
#     # fields = ['owner']
#     form_class = ProfileForm
#     template_name = 'edit-profile.html'
#     success_url = 'my-walks/'

#     def get_initial(self, **kwargs):
#         initial = super().get_initial(**kwargs)
#         initial['owner'] = 'Enter Owner'
#         return initial


class ProfileCreateView(CreateView):
    ''' create a form that people can initially fill out to create their profile. '''
    model = Profile
    fields = ['user', 'owner', 'dog', 'address', 'phonenumber', 'info']
    success_url="my-walks/"


def profile_list(request):
    ''' what model we want to see, where we want to see it '''
    profile = Profile.objects.filter(
        user=request.user.id
    ).first()
    context = {
        "profile": profile if profile else None
    }
    return render(request, "my-walks.html", context)


class AvailabilityList(generic.ListView):
    ''' what model we want to see, where we want to see it
    and the max number of times we want to see it on one page '''
    model = Availability
    template_name = 'book-walk.html'
    paginate_by = 14
