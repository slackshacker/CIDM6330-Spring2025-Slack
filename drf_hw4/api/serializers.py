
# Serializers — Django REST Framework: https://www.django-rest-framework.org/api-guide/serializers/
# This is also touched upon in a couple of the tutorial projects.

# Django REST Framework serializers
from rest_framework import serializers
from .models import Applicant, Contact, Address

# Applicant model
class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'

# Contact model
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

# Address model
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
