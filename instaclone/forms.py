from django import forms
from .models import Profile, InstaPost

class ImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('profile_picture',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = InstaPost
        fields =('picture','post_title','caption',)