"""
URL configuration for cidm6330 project.

Routes requests to the appropriate views. For more information:
https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from ppm.views import root_view  # Custom root endpoint

urlpatterns = [
    path('', root_view),
    path('admin/', admin.site.urls),
    path('api/', include('ppm.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Redirect root to API base
    path('', RedirectView.as_view(url='/api/', permanent=False)),
]
