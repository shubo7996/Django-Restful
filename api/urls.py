"""api URL Configuration
  
  Url Paterns are as follows:

    localhost:8000/admin/ will to redirect to admin's Login
"""
from django.contrib import admin
from django.urls import path,include
from apiService import api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apiService.api_urls')),
    path('apiAuth/',include('rest_framework.urls')),
]
