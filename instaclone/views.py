from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm, ImageFormProfile
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

def index(response):
    return HttpResponse("hello")

def home(response):
    return render(response, "instaclone/home.html")


@login_required
def my_profile(request):
    template = loader.get_template('instaclone/profile.html')
    return HttpResponse(template.render({'profile_pic':profile_pic}, request))

def profile_pic(request):
    if request.method == 'POST':
        form = ImageFormProfile(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ImageFormProfile()
    return render(request, "instaclone/profile_pic.html", {"form":form})


def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ImageForm()
    return render(request, "instaclone/upload.html", {"form":form})




