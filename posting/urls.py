from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('socials/', include('social_django.urls', namespace='social')),    
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('account_activation_sent/', views.ActivationSent.as_view(), name='activationSent'),
    path('activate/<uidb64>/<token>/', views.Activation, name='EmailActivation')
]