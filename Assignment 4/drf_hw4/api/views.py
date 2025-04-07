
# Leveraged from: https://www.django-rest-framework.org/tutorial/quickstart/#views
# and: The completed the following Django "ToDo" tutorials available at: https://www.geeksforgeeks.org/django-tutorial/

from django.shortcuts import render
from rest_framework import viewsets
from .models import Applicant, Contact, Address
from .serializers import ApplicantSerializer, ContactSerializer, AddressSerializer

# Applicant model
class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

# Contact model
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# Address model
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

