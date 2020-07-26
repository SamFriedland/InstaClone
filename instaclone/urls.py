from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('profile_pic/', views.profile_pic, name='profile_pic'),
    path('upload/', views.upload, name='upload'),
    path('home/', views.home, name='home'),
    path('profile/', views.my_profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)