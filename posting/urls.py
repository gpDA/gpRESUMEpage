from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUp, name='signup'),
    #path('verified/', views.Actived, name='activated'),
    path('socials/', include('social_django.urls', namespace='social')),    
    path('ckeditor/', include('ckeditor_uploader.urls')),
    #path('activate/<slug:uidb64>/<slug:token>)/', views.activate, name='activate'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),    

    #path('account_activation_sent/', views.ActivationSent, name='activationSent'),
]