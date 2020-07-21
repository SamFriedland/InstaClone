from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
# Create your views here.

def index(response):
    return HttpResponse("hello")

def profile(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ImageForm()
    return render(request, "instaclone/profile.html", {"form":form})