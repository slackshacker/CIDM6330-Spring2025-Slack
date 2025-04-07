
# Leveraged from: Django ORM – Inserting, Updating & Deleting Data: https://www.geeksforgeeks.org/django-orm-inserting-updating-deleting-data/

from django.db import models

# Create your models here.

# Import Django's base model functionality
from django.db import models

# Writing Models — Django Docs: https://docs.djangoproject.com/en/stable/topics/db/models/
# Field Types Reference: https://docs.djangoproject.com/en/stable/ref/models/fields/

# Applicant model
class Applicant(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DoB = models.DateField()
    Gender = models.CharField(max_length=20)
    ResidencyState = models.CharField(max_length=50)

# Contact model
class Contact(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Applicant_Relationship = models.CharField(max_length=50)

# Address model
class Address(models.Model):
    Street_No = models.CharField(max_length=10)
    Street = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=20)
    Zip = models.CharField(max_length=10)
    Type = models.CharField(max_length=50)
    OwnerID = models.IntegerField()
    OwnerType = models.CharField(max_length=50)

