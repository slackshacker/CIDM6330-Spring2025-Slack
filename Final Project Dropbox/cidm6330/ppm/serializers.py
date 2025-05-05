from rest_framework import serializers
from django.contrib.auth.models import Group, User
from .models import Applicant, Address, Contact

# 🔹 Serializer for Django's built-in User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']

# 🔹 Serializer for Django's built-in Group model
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

# 🔹 Serializer for Applicant model
class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'

# 🔹 Serializer for Address model
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

# 🔹 Serializer for Contact model
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
