from django.urls import path
from . import views

app_name = 'instaclone'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile_pic/', views.change_profile_pic, name='profile_pic'),
    path('upload/', views.upload, name='upload'),
    path('home/', views.home, name='home'),
    path('profile/', views.my_profile, name='profile'),

]
