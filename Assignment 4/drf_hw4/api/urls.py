# Import URL functions and DRF routers
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import ViewSets
from .views import ApplicantViewSet, ContactViewSet, AddressViewSet

# Instantiate DRF's default router
router = DefaultRouter()

# Register each model ViewSet with the router
router.register(r'applicants', ApplicantViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'addresses', AddressViewSet)

# Include the router-generated URLs in urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
