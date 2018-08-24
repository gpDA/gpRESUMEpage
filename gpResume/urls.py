from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('postings/', include('posting.urls')),
    path('', include('project.urls')),
    path('', include('django.contrib.auth.urls')),    
]
