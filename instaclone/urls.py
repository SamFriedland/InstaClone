from django.urls import path, re_path
from . import views


app_name = 'instaclone'
urlpatterns = [
    path('profile_pic/', views.change_profile_pic, name='profile_pic'),
    path('upload/', views.upload, name='upload'),
    path('home/', views.home, name='home'),
    path('my_profile/', views.my_profile, name='my_profile'),
    re_path(r'^profile/(?P<username>\w+)/$', views.profileview, name="profile"),
    re_path(r'^followers/(?P<username>\w+)/$', views.followers, name='followers'),
    re_path(r'^following/(?P<username>\w+)/$', views.following, name='following'),
    re_path(r'^follow/(?P<username>\w+)/$', views.follow, name='follow'),

]
