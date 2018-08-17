from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posting.urls')),
    path('projects/', include('project.urls')),
    path('', include('django.contrib.auth.urls')),    
]
