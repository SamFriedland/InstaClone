from django import forms
from .models import Profile, InstaPost, UserFollowing

class ImageFormProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('profile_picture',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = InstaPost
        fields =('picture','post_title','caption',)

class FollowForm(forms.ModelForm):
    class Meta:
        model = UserFollowing
        fields = ('user_id','following_user_id',)
