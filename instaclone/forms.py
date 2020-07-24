from django import forms
from .models import User, InstaPost

class ImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('profile_picture',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = InstaPost
        fields =('picture','post_title','caption',)