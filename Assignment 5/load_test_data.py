# Django Docs: Creating objects: https://docs.djangoproject.com/en/stable/ref/models/querysets/#create
# “A convenience method for creating an object and saving it all in one step.”

# Python Docs – Argument Unpacking: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
# 4.9.5. Unpacking Argument Lists

# Set up Django environment for standalone execution
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cidm6330.settings")
django.setup()

# Import Django models
from ppm.models import Applicant, Contact, Address

# Load predefined applicant records into the database
def load_applicants():
    applicants = [
        {"FirstName": "Alice", "LastName": "Johnson", "DoB": "1992-06-15", "Gender": "Female", "ResidencyState": "Idaho"},
        {"FirstName": "Bob", "LastName": "Smith", "DoB": "1988-11-22", "Gender": "Male", "ResidencyState": "Idaho"},
        {"FirstName": "Charlie", "LastName": "Brown", "DoB": "1995-04-08", "Gender": "Non-binary", "ResidencyState": "Idaho"},
        {"FirstName": "Diana", "LastName": "King", "DoB": "1980-07-30", "Gender": "Female", "ResidencyState": "Idaho"},
        {"FirstName": "Edward", "LastName": "White", "DoB": "1999-02-14", "Gender": "Male", "ResidencyState": "Idaho"},
        {"FirstName": "Fiona", "LastName": "Adams", "DoB": "1993-09-27", "Gender": "Female", "ResidencyState": "Idaho"},
        {"FirstName": "George", "LastName": "Hill", "DoB": "1985-12-03", "Gender": "Male", "ResidencyState": "Idaho"},
        {"FirstName": "Hannah", "LastName": "Scott", "DoB": "2000-05-19", "Gender": "Female", "ResidencyState": "Idaho"},
        {"FirstName": "Isaac", "LastName": "Thomas", "DoB": "1997-03-10", "Gender": "Male", "ResidencyState": "Idaho"},
        {"FirstName": "Julia", "LastName": "Martin", "DoB": "1990-08-25", "Gender": "Female", "ResidencyState": "Idaho"},
    ]
    for a in applicants:
        Applicant.objects.create(**a)

# Load predefined contact records into the database
def load_contacts():
    contacts = [
        {"First_Name": "Alice", "Last_Name": "Johnson", "Phone": "555-123-4567", "Applicant_Relationship": "Parent"},
        {"First_Name": "Bob", "Last_Name": "Smith", "Phone": "555-234-5678", "Applicant_Relationship": "Guardian"},
        {"First_Name": "Charlie", "Last_Name": "Brown", "Phone": "555-345-6789", "Applicant_Relationship": "Sibling"},
        {"First_Name": "Diana", "Last_Name": "King", "Phone": "555-456-7890", "Applicant_Relationship": "Spouse"},
        {"First_Name": "Edward", "Last_Name": "White", "Phone": "555-567-8901", "Applicant_Relationship": "Parent"},
        {"First_Name": "Fiona", "Last_Name": "Adams", "Phone": "555-678-9012", "Applicant_Relationship": "Guardian"},
        {"First_Name": "George", "Last_Name": "Hill", "Phone": "555-789-0123", "Applicant_Relationship": "Sibling"},
        {"First_Name": "Hannah", "Last_Name": "Scott", "Phone": "555-890-1234", "Applicant_Relationship": "Parent"},
        {"First_Name": "Isaac", "Last_Name": "Thomas", "Phone": "555-901-2345", "Applicant_Relationship": "Guardian"},
        {"First_Name": "Julia", "Last_Name": "Martin", "Phone": "555-012-3456", "Applicant_Relationship": "Spouse"},
    ]
    for c in contacts:
        Contact.objects.create(**c)

# Load predefined address records into the database (previously from address.csv)
def load_addresses():
    addresses = [
        {"Street_No": "123", "Street": "Elm St", "City": "Boise", "State": "ID", "Zip": "83701", "Type": "Home", "OwnerID": 1, "OwnerType": "Self"},
        {"Street_No": "456", "Street": "Maple Ave", "City": "Nampa", "State": "ID", "Zip": "83651", "Type": "Work", "OwnerID": 2, "OwnerType": "Spouse"},
        {"Street_No": "789", "Street": "Oak Blvd", "City": "Meridian", "State": "ID", "Zip": "83642", "Type": "Home", "OwnerID": 3, "OwnerType": "Parent"},
        {"Street_No": "101", "Street": "Pine St", "City": "Caldwell", "State": "ID", "Zip": "83605", "Type": "Home", "OwnerID": 4, "OwnerType": "Guardian"},
        {"Street_No": "202", "Street": "Ash Dr", "City": "Eagle", "State": "ID", "Zip": "83616", "Type": "Work", "OwnerID": 5, "OwnerType": "Self"},
        {"Street_No": "303", "Street": "Cedar Ct", "City": "Kuna", "State": "ID", "Zip": "83634", "Type": "Home", "OwnerID": 6, "OwnerType": "Parent"},
        {"Street_No": "404", "Street": "Birch Ln", "City": "Star", "State": "ID", "Zip": "83669", "Type": "Work", "OwnerID": 7, "OwnerType": "Sibling"},
        {"Street_No": "505", "Street": "Spruce Rd", "City": "Middleton", "State": "ID", "Zip": "83644", "Type": "Home", "OwnerID": 8, "OwnerType": "Spouse"},
        {"Street_No": "606", "Street": "Fir Pl", "City": "Emmett", "State": "ID", "Zip": "83617", "Type": "Work", "OwnerID": 9, "OwnerType": "Self"},
        {"Street_No": "707", "Street": "Willow Way", "City": "Mountain Home", "State": "ID", "Zip": "83647", "Type": "Home", "OwnerID": 10, "OwnerType": "Guardian"},
    ]
    for addr in addresses:
        Address.objects.create(**addr)

# Main function to run all loaders
def run_all():
    print("Loading Applicants...")
    load_applicants()
    print("Applicants loaded.")

    print("Loading Contacts...")
    load_contacts()
    print("Contacts loaded.")

    print("Loading Addresses...")
    load_addresses()
    print("Addresses loaded.")

# Execute when run as a script
if __name__ == "__main__":
    run_all()
