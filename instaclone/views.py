from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

def index(response):
    return HttpResponse("hello")

def home(response):
    return HttpResponse("home")


@login_required
def my_profile(request):
    template = loader.get_template('instaclone/profile.html')
    context = {'Profile.username':Profile.username}
    return HttpResponse(template.render(context, request))

def profile_pic(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ImageForm()
    return render(request, "instaclone/profile_pic.html", {"form":form})


def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ImageForm()
    return render(request, "instaclone/upload.html", {"form":form})




