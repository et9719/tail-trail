''' Imports '''
from django.shortcuts import render
from django.views import generic
from .models import Availability, Profile


def profile_list(request):
    ''' what model we want to see, where we want to see it '''
    profile = Profile.objects.filter(
        user=request.user.id
    ).first()
    context = {
        "profile": profile if profile else None
    }
    return render(request, "my-walks.html", context)


def profile_create(request):
    ''' what model we want to see, where we want to see it '''
    if request.method == "GET":
        profile = Profile.objects.filter(
            user=request.user.id
        ).first()
        context = {
            "profile": profile if profile else None
        }
        return render(request, "profile_create_form.html", context)
    if request.method == "POST":
        profile = Profile(
            user=request.user,
            owner=request.POST.get("owner"),
            dog=request.POST.get("dog"),
            address=request.POST.get("address"),
            phonenumber=request.POST.get("phonenumber"),
            info=request.POST.get("info"),
        )
        profile.save()
        context = {
            "profile": profile
        }
        return render(request, "my-walks.html", context)


def profile_update(request):
    ''' what model we want to see, where we want to see it '''
    if request.method == "GET":
        profile = Profile.objects.filter(
            user=request.user.id
        ).first()
        context = {
            "profile": profile if profile else None
        }
        return render(request, "profile_update_form.html", context)
    if request.method == "POST":
        profile = Profile(
            user=request.user,
            owner=request.POST.get("owner"),
            dog=request.POST.get("dog"),
            address=request.POST.get("address"),
            phonenumber=request.POST.get("phonenumber"),
            info=request.POST.get("info"),
        )
        profile.save()
        context = {
            "profile": profile
        }
        return render(request, "my-walks.html", context)


class AvailabilityList(generic.ListView):
    ''' what model we want to see, where we want to see it
    and the max number of times we want to see it on one page '''
    model = Availability
    template_name = 'book-walk.html'
    paginate_by = 14
