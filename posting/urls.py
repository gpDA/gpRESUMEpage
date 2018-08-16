from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('socials/', include('social_django.urls', namespace='social')),    
    path('ckeditor/', include('ckeditor_uploader.urls')),
]