from django.contrib import admin  
from django.urls import path, include  
from rest_framework import routers


urlpatterns = [  
    path('admin/', admin.site.urls),
    path('api/problem/', include('problems.urls')),  # Dedicated path for 'problems' app
    path('api/note/', include('notes.urls')),  # Dedicated path for 'notes' app
]