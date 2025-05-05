from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    api_root, launch_tasks,
    UserViewSet, GroupViewSet,
    ApplicantViewSet, AddressViewSet, ContactViewSet,
)

# DRF Router for ViewSets
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'applicants', ApplicantViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', api_root),
    path('', include(router.urls)),
    path('launch-tasks/', launch_tasks),
]
