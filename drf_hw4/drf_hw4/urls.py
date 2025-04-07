"""
URL configuration for drf_hw4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Import required modules
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "PROJECT TITLE": "CIDM 6330, Assignment 04 - Migrate to Django DRF API.",
        "Project endpoints": [
            "/api/applicants/",
            "/api/contacts/",
            "/api/addresses/"
        ]
    })

# Define URL patterns for the project
urlpatterns = [
    # Added root route to avoid the Page not found (404), Request Method: GET Request URL: 	http://127.0.0.1:8000/
    path('', api_root), 

    # Django Admin route                    
    path('admin/', admin.site.urls),

    # Include the API app's routes        
    path('api/', include('api.urls')),      
]
