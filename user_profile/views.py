from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import UserProfile
from .forms import CommentForm


class ProfileList(generic.ListView):
    model = UserProfile
    # date_joined is part of User i believe, can i ref it here through UserProfile?
    queryset = UserProfile.objects.order_by('-date_joined')
    template_name = 'profile_list.html'


class ProfileDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Profile.objects.filter(status=1)
        profile = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')

        return render(request, "profile_detail.html", { },)

        # is this where i add logic for a user editing own profile?

        # is this where i add to show only users posts or link the normal blog post view and logic i the html file?
