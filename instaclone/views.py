from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ImageForm, ImageFormProfile, FollowForm
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse
from instaclone.models import InstaPost, UserFollowing, Profile
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
# Create your views here.

def index(response):
    return HttpResponse("hello")

def home(response):
    return render(response, "instaclone/home.html")


@login_required
def my_profile(request):
    template = loader.get_template('instaclone/my_profile.html')
    return HttpResponse(template.render({}, request))

def change_profile_pic(request):
    if request.method == 'POST':
        form = ImageFormProfile(request.POST,request.FILES)
        if form.is_valid():
            user=request.user
            user.profile.profile_picture = request.FILES.get('profile_picture',user.profile.profile_picture)
            user.profile.save()
            form.save()

            return HttpResponseRedirect(reverse('instaclone:my_profile'))
    else:
        form=ImageFormProfile()
    return render(request, "instaclone/profile_pic.html", {"form":form})



def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            user=request.user
            p=InstaPost(
                user = user.profile,
                picture = request.FILES.get('picture'),
                post_title = form.cleaned_data.get('post_title'),
                caption = form.cleaned_data.get('caption'),
                pub_date = timezone.now()

            )

            p.save()
            form.save()
            return HttpResponseRedirect(reverse('instaclone:my_profile'))
    else:
        form=ImageForm()
    return render(request, "instaclone/upload.html", {"form":form})




def followers(request, username):
    user = User.objects.get(username=username)
    template = loader.get_template('instaclone/followers.html')
    return HttpResponse(template.render({'user':user}, request))

def following(request, username):
    user = User.objects.get(username=username)
    template = loader.get_template('instaclone/following.html')
    return HttpResponse(template.render({'user':user}, request))

def profileview(request, username):
    user_profile = User.objects.get(username=username)
    template = loader.get_template('instaclone/profile.html')
    return HttpResponse(template.render({'user_profile':user_profile}, request))

def follow(request, username):
    user = User.objects.get(username=username)
    template = loader.get_template('instaclone/follow.html')
    return HttpResponse(template.render({'user':user}, request))





