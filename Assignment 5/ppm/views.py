from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Applicant, Address, Contact
from .serializers import (
    GroupSerializer, UserSerializer,
    ApplicantSerializer, AddressSerializer, ContactSerializer
)

from .tasks import simulate_long_task

# 📌 Root view for the home page
@api_view(['GET'])
def root_view(request):
    return Response({
        "message": "Welcome to the CIDM 6330 API",
        "api_base": "/api/"
    })

# 📌 API root overview endpoint
@api_view(['GET'])
def api_root(request):
    return Response({
        "info": "CIDM 6330 - Unified DRF API with SQLite",
        "endpoints": {
            "applicants": "/api/applicants/",
            "addresses": "/api/addresses/",
            "contacts": "/api/contacts/",
            "launch_tasks": "/api/launch-tasks/",
        }
    })

# 📌 User API view (DRF ViewSet)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# 📌 Group API view (DRF ViewSet)
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# 📌 Applicant API endpoint
class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

# 📌 Address API endpoint
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

# 📌 Contact API endpoint
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# 📌 Launch 10 async Celery tasks, spaced 30 seconds apart
@api_view(['POST'])
def launch_tasks(request):
    for i in range(10):
        simulate_long_task.apply_async(
            args=[f"Task {i+1}", 5],
            countdown=i * 30
        )
    return Response({"message": "10 tasks scheduled with 30-second intervals."})
