from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile_pic/', views.profile_pic, name='profile_pic'),
    path('upload/', views.upload, name='upload'),



]