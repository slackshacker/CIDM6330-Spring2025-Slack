# Execute with:
# python manage.py test ppm --verbosity=2
# To print each test scenario as it executes to any trace failures or errors.

import time
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Applicant, Address, Contact

# ----------------------------------
# Test Initialization Class
# ----------------------------------
class SlowTestBase(APITestCase):
    # Adds a delay between test method executions to allow for manual observation
    delay_between_tests = 60  # Seconds

    def setUp(self):
        # Setup reusable test data and authenticated client.
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

        # Create an instance of each model to work with.
        self.applicant = Applicant.objects.create(
            FirstName="John", LastName="Doe", DoB="1990-01-01",
            Gender="Male", ResidencyState="Texas"
        )

        self.address = Address.objects.create(
            Street_No="123", Street="Main St", City="Amarillo",
            State="TX", Zip="79101", Type="Home",
            OwnerID=self.applicant.id, OwnerType="Applicant"
        )

        self.contact = Contact.objects.create(
            First_Name="Jane", Last_Name="Smith",
            Phone="5551234567", Applicant_Relationship="Sister"
        )

    def run(self, result=None):
        # Adds a delay after each test run for better visual monitoring.
        super().run(result)
        time.sleep(self.delay_between_tests)


# Discovered due to errors with my use of 'scenario_' instead of 'test_'.
"""
Django Documentation Reference:
    Django will look for any class that inherits from `unittest.TestCase` 
    (including `django.test.TestCase`) and any method that starts with `test_`.

    “A test case is a class that inherits from `django.test.TestCase`. Django 
    will find tests in any file whose name begins with `test`, and the test 
    runner will discover test methods prefixed with `test_`.”

    This naming convention is inherited from the `unittest` framework, which 
    Django extends.

    Django Software Foundation. (2024). Testing in Django: Writing tests. Django documentation (v5.2). 
    https://docs.djangoproject.com/en/stable/topics/testing/overview/#writing-tests
"""
# ----------------------
# The Applicant CRUD Testing
# ----------------------
class ApplicantTests(SlowTestBase):

    # Valid create (post), expected result: PASS.
    def test_create_applicant_with_valid_data(self):
        data = {
            "FirstName": "Alice", "LastName": "Walker",
            "DoB": "1985-04-12", "Gender": "Female", "ResidencyState": "Colorado"
        }
        response = self.client.post('/api/applicants/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Missing required field, expected result: FAIL with 400.
    def test_create_applicant_with_missing_field(self):
        data = {
            "LastName": "Walker", "DoB": "1985-04-12", "Gender": "Female"
        }
        response = self.client.post('/api/applicants/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Valid retrieve (get), expected result: PASS.
    def test_retrieve_applicant_detail(self):
        response = self.client.get(f'/api/applicants/{self.applicant.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Valid update (put), expected result: PASS.
    def test_update_applicant(self):
        data = {
            "FirstName": "John", "LastName": "Doe",
            "DoB": "1991-01-01", "Gender": "Male", "ResidencyState": "New Mexico"
        }
        response = self.client.put(f'/api/applicants/{self.applicant.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Valid delete, expected result: PASS.
    def test_delete_applicant(self):
        response = self.client.delete(f'/api/applicants/{self.applicant.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# --------------------
# The Address CRUD Testing
# --------------------
class AddressTests(SlowTestBase):

    # Valid create (post), expected result: PASS.    
    def test_create_address_with_valid_data(self):
        data = {
            "Street_No": "456", "Street": "Oak St", "City": "Dallas",
            "State": "TX", "Zip": "75201", "Type": "Work",
            "OwnerID": self.applicant.id, "OwnerType": "Applicant"
        }
        response = self.client.post('/api/addresses/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Valid retrieve (get), expected result: PASS.
    def test_get_address_list(self):
        response = self.client.get('/api/addresses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Valid update (put), expected result: PASS.
    def test_update_address(self):
        data = {
            "Street_No": "789", "Street": "Elm St", "City": "Austin",
            "State": "TX", "Zip": "73301", "Type": "Home",
            "OwnerID": self.applicant.id, "OwnerType": "Applicant"
        }
        response = self.client.put(f'/api/addresses/{self.address.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Valid delete, expected result: PASS.
    def test_delete_address(self):
        response = self.client.delete(f'/api/addresses/{self.address.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# --------------------
# The Contact CRUD Testing
# --------------------
class ContactTests(SlowTestBase):

    # Valid create (post), expected result: PASS.   
    def test_create_contact_with_valid_data(self):
        data = {
            "First_Name": "Bob", "Last_Name": "Jones",
            "Phone": "5559876543", "Applicant_Relationship": "Uncle"
        }
        response = self.client.post('/api/contacts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Valid retrieve (get), expected result: PASS.
    def test_get_contact_detail(self):
        response = self.client.get(f'/api/contacts/{self.contact.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Valid update (put), expected result: PASS.
    def test_update_contact(self):
        data = {
            "First_Name": "Jane", "Last_Name": "Smith",
            "Phone": "5550001111", "Applicant_Relationship": "Mother"
        }
        response = self.client.put(f'/api/contacts/{self.contact.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Valid delete, expected result: PASS.
    def test_delete_contact(self):
        response = self.client.delete(f'/api/contacts/{self.contact.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# ----------------------------
# The Admin-only Access Test Cases
# ----------------------------
class AdminAccessTests(SlowTestBase):

    # Unauthorized access to admin panel, expected result: FAIL.
    def test_non_admin_user_cannot_access_admin_panel(self):
        # Attempt to access Django admin panel HTML (unauthorized users are redirected to login)
        response = self.client.get('/admin/', follow=True)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    # Valid admin access, expected result: PASS.
    def test_admin_user_can_access_admin_panel(self):
        # Create a superuser and authenticate
        admin_user = User.objects.create_superuser(username='adminuser', password='adminpass', email='admin@example.com')
        self.client.force_authenticate(user=admin_user)

        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Unauthorized user creation, expected result: FAIL with (403 or 401).
    def test_non_admin_cannot_create_user(self):
        # Only superusers should ideally be able to POST to /api/users/
        data = {
            "username": "anotheruser",
            "email": "new@example.com",
            "is_staff": False
        }
        response = self.client.post('/api/users/', data, format='json')
        self.assertIn(response.status_code, [status.HTTP_403_FORBIDDEN, status.HTTP_401_UNAUTHORIZED])

    # Valid admin user creation, expected result: PASS.
    def test_admin_can_create_user(self):
        # Superuser creates a new user via API (assumes API is configured to allow admin POST)
        admin_user = User.objects.create_superuser(username='admin2', password='adminpass', email='admin2@example.com')
        self.client.force_authenticate(user=admin_user)

        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "is_staff": False
        }
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
