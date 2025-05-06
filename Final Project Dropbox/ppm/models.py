from django.db import models

# Applicant model to represent individual applicant records
class Applicant(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DoB = models.DateField()
    Gender = models.CharField(max_length=20)
    ResidencyState = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

# Address model to store mailing and physical address records
class Address(models.Model):
    Street_No = models.CharField(max_length=10)
    Street = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zip = models.CharField(max_length=10)
    Type = models.CharField(max_length=50)  # e.g., Home, Work
    OwnerID = models.IntegerField()         # ID of the entity this address belongs to
    OwnerType = models.CharField(max_length=50)  # e.g., 'Applicant', 'Contact'

    def __str__(self):
        return f"{self.Street_No} {self.Street}, {self.City}"

# Contact model for emergency or supporting contacts
class Contact(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Applicant_Relationship = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"
