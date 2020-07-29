from django.shortcuts import render, redirect
from .forms import RegisterForm
from instaclone.models import Profile



# Create your views here.

def register(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            profile=Profile.objects.create(
                user = user,
                username = form.cleaned_data['username'],
                d_o_b = form.cleaned_data['d_o_b']
            )

            profile.save()
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form,})

