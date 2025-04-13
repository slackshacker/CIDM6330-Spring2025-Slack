# West Texas A&M University - CIDM 6330-70

**Title:** Assignment 05: Complete Django Migration

**Description:** Evolution 5 of the CIDM 6330-70 course project.

**Author:** David Slack

**Created Date:** 2025.04.07

**Last Modified:** 2025.04.07

**Document Status:** Final

**Document Version:** 1.0.0

# Assignment Descripton & Deliverables (per the course outline instructions):
## Instructions 
### Assignment 05: Complete Django Migration
At this stage, we should have the following:

- Entity structural and behavioral design and implementation - Django Models will work for the most part
- A Django-based API - DRF or Django Ninja
- A persistence O/RM in Django (in place of the repository pattern)
- An event queue with Celery
- An event queue processor with Redis

What we are after now is to wrap all of this up with tests.  
        
#### Steps to Take
*OLD STEPS THAT YOU'VE TAKEN PREVIOUSLY:* You should have the following in place:
1. Django O/RM for repository
2. Translate your API into one that uses the Django REST Framework (or Django Ninja)
3. Messaging and Events with Celery/Redis
    
*NEW STEPS FOR THIS ASSIGNMENT:* Now, we'll implement Unit Testing with the built-in Django unit-test: Testing in Django | Django documentation | Django:
1. Extend your API beyond CRUD to perform a few operations that are consistent with your design
2. At least some of these operations should include placing tasks on workers and task queues in Celery/Redis
3. Create tests for these methods using Django's Unit test framework
        
#### API CRUD + Repository Persistence

The purpose of this assignment is to complete our architecture with testing.  Despite being a web application framework, we are *NOT* building any UI elements; all will be proven through tests.

### Evolution_05_TDD_BDD_DDD
#### Designing from Evidence
We should have made this the first evolution, but there are cart and horse issues here.

#### Test-Driven Development
- [Test-Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html) 
    - Write a test for the next bit of functionality you want to add.
    - Write the functional code until the test passes.
    - Refactor both new and old code to make it well structured.
- [Behavior Driven Development](https://cucumber.io/docs/bdd/)
    - ***Discovery (what it could do)***: Given a User Story that describes the system, decompose this into the tasks that will realize the functionality and development details that will lead to the developmment of the artifacts that satisfy the story.
    - ***Formulation (what it should do)***: Document tasks so that they can be validated through automated testing.
    - ***Automation (what it actually does)***: Implement the tasks such that they produce the behaviours needed and prove the behaviours through automated tests.
- [Domain Driven Design](https://martinfowler.com/bliki/DomainDrivenDesign.html)

#### Requirements

1. For DDD create a ubiquitous language glossary: [https://thedomaindrivendesign.io/developing-the-ubiquitous-language/](https://thedomaindrivendesign.io/developing-the-ubiquitous-language/)
    1. wayback archive: [https://web.archive.org/web/20241122220908/https://thedomaindrivendesign.io/developing-the-ubiquitous-language/](https://web.archive.org/web/20241122220908/https://thedomaindrivendesign.io/developing-the-ubiquitous-language/)

2. For BDD create A Gherkin Notation expression for each test: [Gherkin Syntax](https://cucumber.io/docs/gherkin/)
3. For TDD create tests that correspond with your Gherkin Statements.

# My Approach:
To complete this assignment and continue from the previous, I took a learn-by-doing/hands-on and structured approach. First, I went through all the course materials—textbook, lectures, videos, and any extra resources that were recommended. In addition I followed the tutorials outlinded below as a starting point for working with Django REST Framework. I also completed the official DRF quickstart tutorial for creating a simple API that lets admin users manage users and groups. The final step is where I started a new project using Django REST Framework and integrated the structures built in **Assignment 04: Migrate to Django**.

*The https://www.geeksforgeeks.org/ tutorials and documentation were a substantial aid in understanding the Django REST Framework.*

1. Review the course materials: text, lectures, videos, and recommended supplemental references.
2. Completed the Django tutorial "Building Web APIs with Django Rest Framework: A Beginner's Guide" available at: https://betterstack.com/community/guides/scaling-python/introduction-to-drf/?utm_source=chatgpt.com
3. Completed the following Django tutorials available at: https://www.geeksforgeeks.org/django-tutorial/
    - ToDo webapp using Django
4. Completed the tutorial to "create a simple API to allow admin users to view and edit the users and groups in the system" available at: https://www.django-rest-framework.org/tutorial/quickstart/#project-setup
5. Completed the tutorial "How to Create a basic API using Django Rest Framework?" available at: https://www.geeksforgeeks.org/how-to-create-a-basic-api-using-django-rest-framework/
6. **Created a new project**, *now renamed CIDM6630 reflecting a course level project*, using the Djanog REST Framework and integrate the prevous structures from *Assignments 3 and 4* into the project using https://www.django-rest-framework.org/tutorial/quickstart/ as a reference.
7. Stepped through the test requirements as outlined in the *Evolution_05_TDD_BDD_DDD* README.MD for additional clarity on expectations in contrast to the *Assignment 5: Full Django + Tests* instructions.

    - [Test-Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html) 
        - Write a test for the next bit of functionality you want to add.
        - Write the functional code until the test passes.
        - Refactor both new and old code to make it well structured.
    - [Behavior Driven Development](https://cucumber.io/docs/bdd/)
        - ***Discovery (what it could do)***: Given a User Story that describes the system, decompose this into the tasks that will realize the functionality and development details that will lead to the developmment of the artifacts that satisfy the story.
        - ***Formulation (what it should do)***: Document tasks so that they can be validated through automated testing.
        - ***Automation (what it actually does)***: Implement the tasks such that they produce the behaviours needed and prove the behaviours through automated tests.
    - [Domain Driven Design](https://martinfowler.com/bliki/DomainDrivenDesign.html)

# Django Rest Framework Project: **CIDM6330**
Included for my future reference are the series of commands, executed in sequence, to create the project, establish the virtual environment, run the application, and evaluate the results and capture the appropriate screen captures.

## Project setup
Follows the example at: https://www.django-rest-framework.org/tutorial/quickstart/
### 1. Create the project directory
- mkdir **cidm6330**
- cd **cidm6330**

### 2. Create a virtual environment to isolate the package dependencies locally
This is to avoid dependency conflicts with other the other Python projects on the system. Once the viratual environment is activated, the prompt should change to show (venv), the name of the virtual environment. Any Python packages installed now will be local to this project.

- python -m venv ppmvenv
- ppmvenv\Scripts\activate # Windows

### 3. Install Django and Django REST framework into the virtual environment
- pip install djangorestframework       

### 4. Set up a new project with a single application
Start a new Django project inside the current folder ("."). 
- django-admin startproject **cidm6330** .   

### 5. Create the new Django app named "ppm"
This is where I'll build models, serializers, views, etc. to support the application.

- django-admin startapp ppm

#### This creates the following folder structure:
*manage.py is the entry point for most Django commands, i.e. "python manage.py makemigrations" and "python manage.py migrate" that will be used later.*

- \cidm6330\cidm6330\ - **Project folder**
- \cidm6330\cidm6330\asgi.py
- \cidm6330\cidm6330\settings.py
- \cidm6330\cidm6330\urls.py
- \cidm6330\cidm6330\wsgi.py
- \cidm6330\cidm6330\__init__.py
- \cidm6330\ppm\ - **API Folder**
- \cidm6330\manage.py
- \cidm6330\ppm\migrations\
- \cidm6330\ppm\admin.py
- \cidm6330\ppm\apps.py
- \cidm6330\ppm\models.py
- \cidm6330\ppm\tests.py
- \cidm6330\ppm\views.py
- \cidm6330\ppm\__init__.py
- \cidm6330\ppm\migrations\__init__.py
- \cidm6330\ppmvenv\ - **Virtual Environment**

## Run and Validate the Application

Install Django and Django REST Framework and any other desired packages. Note: Installs only for this vm instance.
- pip install django djangorestframework

Apply the project Migrations to Create the Database
Run Django's migration system to set up the database (SQLite):
- python manage.py makemigrations
- python manage.py migrate

Load my Initial Test Data Leveraged Homework 3.
- python manage.py shell
- from api.load_test_data import run_all
- run_all()
- exit()

Create two Superusers to test with.
- python manage.py createsuperuser --username admin --email admin@example.com
- python manage.py createsuperuser --username david --email david@slackshack.net

Now Run the Development Server to Confirm Everything is in Place

- (ppmvenv) PS D:\cidm6330> python manage.py runserver

> Watching for file changes with StatReloader
>Performing system checks...
>
>System check identified no issues (0 silenced).
>April 12, 2025 - 23:01:35
>Django version 5.1.8, using settings 'cidm6330.settings'
>Starting development server at http://127.0.0.1:8000/
>Quit the server with CTRL-BREAK.

## Access the Application URLs with a Browser
- API Root: http://127.0.0.1:8000/
- API Endpoints: http://127.0.0.1:8000/api/
- Django Admin: http://127.0.0.1:8000/admin/

# Project Contents & Artifacts (Deliverables)

## Domain Driven Design
Utilizing the definition and example at: https://thedomaindrivendesign.io/developing-the-ubiquitous-language/
## The Project (Ubiquitous Language) Glossary

| **Term**               | **Ubiquitous Domain Definition** |
|------------------------|----------------------------------|
| **Applicant**          | A person seeking to apply for enrollment, services, or access to a program. An Applicant is the primary entity whose identity, address, and contacts are being managed. |
| **Address**            | A physical or mailing location tied to an Applicant. It includes structured fields like street, city, state, ZIP code, and address type (e.g., "Home", "Work"). Addresses are not standalone, they are tied to an owning entity. |
| **OwnerType**          | A field that expresses the kind of entity that owns an address, such as `"Applicant"` or potentially `"Contact"` (if supported).  |
| **OwnerID**            | The unique identifier for the object (e.g., an Applicant) to which an address belongs. This reinforces entity ownership. |
| **Contact**            | A secondary individual associated with an Applicant, such as a relative, legal guardian, or emergency contact. A Contact is typically defined by name, relationship, and phone number. |
| **Relationship**       | The nature of the association between the Contact and the Applicant, such as "Mother", "Spouse", "Legal Guardian", etc. It is a required field for understanding contact context. |
| **User**               | An authenticated individual accessing the system. Users may be staff, admins, or API clients authorized to perform CRUD actions on the domain. |
| **Admin (Superuser)**  | A special user with unrestricted access to the Django Admin Panel and sensitive operations like user creation and group assignment. |
| **Applicant Repository** | This refers to the abstraction (Django ViewSet) that handles persistence and retrieval of Applicants. A similar object exists for Addresses and Contacts. |
| **Command**            | An action that changes state in the domain, such as “create applicant,” “update address,” or “delete contact.” In this project, these are expressed as HTTP `POST`, `PUT`, and `DELETE` style actions. |
| **Event (Celery Task)**| A domain-relevant background activity, such as `simulate_long_task`, that models asynchronous behavior within the business rules context.  |
| **Applicant API**      | A context within the API dedicated to managing the lifecycle of Applicant entities, including their personal data and lifecycle changes. |
| **CRUD Operations**    | Create, Read, Update, Delete — the essential operations for managing domain entities such as Applicants, Addresses, and Contacts. |
| **Validation Error(s)**   | The feedback mechanism returned by the system when submitted data violates business rules (e.g., missing required fields or incorrect formats). |
| **HTTP Status Codes**  | Domain-specific response mechanisms to communicate the result of a command. Example, `201 Created`, `400 Bad Request`, `403 Forbidden`, `404 Not Found`. |

## Test-Driven Development
*"For BDD create A Gherkin Notation expression for each test: [Gherkin Syntax](https://cucumber.io/docs/gherkin/)"*

### *Gherkin Notation*
Note: A lot of cut/paste/modify!
Two sets of test were identified: 
- api_tests_implemented.feature
- api_tests_not_implemented.feature

Although the *not implemented* tests were identified as practical scenarios, time constraints led to prioritizing the tests that were implemented. Beslow is the listing of *implemented* test scenarios.

### Feature: Applicant Management

#### Scenario: Create a valid applicant
- **Given** I am an authenticated user  
- **When** I submit a valid applicant creation request  
- **Then** the system should return a **201 CREATED** response  

#### Scenario: Create applicant with missing field
- **Given** I am an authenticated user  
- **When** I submit an applicant request with missing required fields  
- **Then** the system should return a **400 BAD REQUEST** response  

#### Scenario: Retrieve an existing applicant
- **Given** I am an authenticated user  
- **And** an applicant exists  
- **When** I retrieve the applicant by ID  
- **Then** the system should return a **200 OK** response with applicant details  

#### Scenario: Update an existing applicant
- **Given** I am an authenticated user  
- **And** an applicant exists  
- **When** I submit a full update with valid data  
- **Then** the system should return a **200 OK** response  

#### Scenario: Delete an applicant
- **Given** I am an authenticated user  
- **And** an applicant exists  
- **When** I send a delete request for the applicant  
- **Then** the system should return a **204 NO CONTENT** response  


### Feature: Address Management

#### Scenario: Create a valid address
- **Given** I am an authenticated user  
- **And** an applicant exists  
- **When** I submit a valid address creation request  
- **Then** the system should return a **201 CREATED** response  

#### Scenario: Retrieve the list of addresses
- **Given** I am an authenticated user  
- **When** I retrieve the list of addresses  
- **Then** the system should return a **200 OK** response with address data  

#### Scenario: Update an existing address
- **Given** I am an authenticated user  
- **And** an address exists  
- **When** I submit a full update to the address  
- **Then** the system should return a **200 OK** response  

#### Scenario: Delete an address
- **Given** I am an authenticated user  
- **And** an address exists  
- **When** I send a delete request for the address  
- **Then** the system should return a **204 NO CONTENT** response  


### Feature: Contact Management

#### Scenario: Create a valid contact
- **Given** I am an authenticated user  
- **When** I submit a valid contact creation request  
- **Then** the system should return a **201 CREATED** response  

#### Scenario: Retrieve a contact by ID
- **Given** I am an authenticated user  
- **And** a contact exists  
- **When** I retrieve the contact by ID  
- **Then** the system should return a **200 OK** response  

#### Scenario: Update an existing contact
- **Given** I am an authenticated user  
- **And** a contact exists  
- **When** I submit a full update to the contact  
- **Then** the system should return a **200 OK** response  

#### Scenario: Delete a contact
- **Given** I am an authenticated user  
- **And** a contact exists  
- **When** I send a delete request for the contact  
- **Then** the system should return a **204 NO CONTENT** response  


### Feature: Admin Access Control

#### Scenario: Non-admin cannot access admin panel
- **Given** I am logged in as a non-admin user  
- **When** I try to access the Django admin panel  
- **Then** the system should redirect or deny access  

#### Scenario: Admin can access admin panel
- **Given** I am logged in as a superuser  
- **When** I access the Django admin panel  
- **Then** the system should return a **200 OK** response  

#### Scenario: Non-admin cannot create a user via API
- **Given** I am logged in as a non-admin user  
- **When** I send a request to create a new user  
- **Then** the system should return a **403 FORBIDDEN** or **401 UNAUTHORIZED**  

#### Scenario: Admin can create a user via API
- **Given** I am logged in as a superuser  
- **When** I send a request to create a new user  
- **Then** the system should return a **201 CREATED** response  

## Test-Driven Development
*For TDD create tests that correspond with your Gherkin Statements.*

The tests are also available in **\cidm6330\ppm\tests.py**

These tests were executed and debugged during the process of development.

```python
"""
# Execute with:
# python manage.py test ppm --verbosity=2
# To print each test scenario as it executes to trace failures or errors.

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

"""
```
# API Endpoint List
Utilized to validate the application, routes, and testing.

| Endpoint | Method(s) | Description |
|----------|-----------|-------------|
| [http://127.0.0.1:8000/](http://127.0.0.1:8000/) | GET | **Root View** — Returns a welcome message and reference to API base path. |
| [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) | GET | **API Root Overview** — Lists main resources and task-launching endpoint. |
| [http://127.0.0.1:8000/api/users/](http://127.0.0.1:8000/api/users/) | GET, POST | **User List/Create** — Manage users (auth required). |
| [http://127.0.0.1:8000/api/users/{id}/](http://127.0.0.1:8000/api/users/{id}/) | GET, PUT, PATCH, DELETE | **User Detail** — View, update, or delete a user (auth required). |
| [http://127.0.0.1:8000/api/groups/](http://127.0.0.1:8000/api/groups/) | GET, POST | **Group List/Create** — Manage user groups (auth required). |
| [http://127.0.0.1:8000/api/groups/{id}/](http://127.0.0.1:8000/api/groups/{id}/) | GET, PUT, PATCH, DELETE | **Group Detail** — View, edit, or delete a group (auth required). |
| [http://127.0.0.1:8000/api/applicants/](http://127.0.0.1:8000/api/applicants/) | GET, POST | **Applicant List/Create** — Manage applicant records. |
| [http://127.0.0.1:8000/api/applicants/{id}/](http://127.0.0.1:8000/api/applicants/{id}/) | GET, PUT, PATCH, DELETE | **Applicant Detail** — Modify an individual applicant. |
| [http://127.0.0.1:8000/api/addresses/](http://127.0.0.1:8000/api/addresses/) | GET, POST | **Address List/Create** — Manage applicant or contact addresses. |
| [http://127.0.0.1:8000/api/addresses/{id}/](http://127.0.0.1:8000/api/addresses/{id}/) | GET, PUT, PATCH, DELETE | **Address Detail** — Update or retrieve address info. |
| [http://127.0.0.1:8000/api/contacts/](http://127.0.0.1:8000/api/contacts/) | GET, POST | **Contact List/Create** — Manage contact records. |
| [http://127.0.0.1:8000/api/contacts/{id}/](http://127.0.0.1:8000/api/contacts/{id}/) | GET, PUT, PATCH, DELETE | **Contact Detail** — View or modify contact info. |
| [http://127.0.0.1:8000/api/launch-tasks/](http://127.0.0.1:8000/api/launch-tasks/) | POST | **Celery Task Trigger** — Launches 10 async tasks spaced 30 seconds apart. Must use: `curl -X POST http://127.0.0.1:8000/api/launch-tasks/` |
| [http://127.0.0.1:8000/api-auth/login/](http://127.0.0.1:8000/api-auth/login/) | GET, POST | **Browsable API Login** — Session login for DRF interface. |
| [http://127.0.0.1:8000/api-auth/logout/](http://127.0.0.1:8000/api-auth/logout/) | GET | **Browsable API Logout** — Ends the session. |
| [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) | GET, POST | **Django Admin Panel** — Full-featured interface to manage users, data, and models. |


# Project Screen Captures
## Root View: http://127.0.0.1:8000/ Image
![http://127.0.0.1:8000/ Image](Root_View.jpg)

## Root View API Root: http://127.0.0.1:8000/api/ Image
![http://127.0.0.1:8000/api/ Image](Root_View_API_Root.jpg)

## Root View API Root Address List: http://127.0.0.1:8000/api/addresses/ Image
![http://127.0.0.1:8000/api/addresses/ Image](Root_View_API_Root_Address_List.jpg)

## Root View API Root Applicant List: http://127.0.0.1:8000/api/applicants/ Image
![http://127.0.0.1:8000/api/applicants/ Image](Root_View_API_Root_Applicant_List.jpg)

## Root View API Root Applicant Instance: http://127.0.0.1:8000/api/applicants/{id}/ Image
![http://127.0.0.1:8000/api/applicants/{id}/ Image](Root_View_API_Root_Applicant_Instance.jpg)

## Root View API Root Group Instance: http://127.0.0.1:8000/api/groups/{id}/ Image
![http://127.0.0.1:8000/api/groups/{id}/ Image](Root_View_API_Root_Group_Instance.jpg)

## Root View API Root User List: http://127.0.0.1:8000/api/users/ Image
![http://127.0.0.1:8000/api/users/ Image](Root_View_API_Root_User_List.jpg)

## Root View API Root User Instance: http://127.0.0.1:8000/api/users/{id}/ Image
![http://127.0.0.1:8000/api/users/{id}/ Image](Root_View_API_Root_User_Instance.jpg)

## Django Admin Login: http://127.0.0.1:8000/admin/ Image
![http://127.0.0.1:8000/admin/ Image](Django_Admin_Login.jpg)

## Django Admin: http://127.0.0.1:8000/admin/ Image
![http://127.0.0.1:8000/admin/ Image](Django_Admin.jpg)

## Django Admin Groups: http://127.0.0.1:8000/admin/ Image
![http://127.0.0.1:8000/admin/ Image](Django_Admin_Groups.jpg)

## Django Admin Users: http://127.0.0.1:8000/admin/ Image
![http://127.0.0.1:8000/admin/ Image](Django_Admin_Users.jpg)

## Django Admin Task Results: http://127.0.0.1:8000/admin/ Image
![http://127.0.0.1:8000/admin/ Image](Django_Admin_Task_Results.jpg)

## Django Admin Addresses: http://127.0.0.1:8000/admin/ Image
![http://127.0.0.1:8000/admin/ Image](Django_Admin_Addresses.jpg)

## Django Admin Applicants: http://127.0.0.1:8000/admin/ Image
![http://127.0.0.1:8000/admin/ Image](Django_Admin_Applicants.jpg)

## Django Admin Contacts: http://127.0.0.1:8000/admin/ Image
![http://127.0.0.1:8000/admin/ Image](Django_Admin_Contacts.jpg)

## Celery Task Processing: Terminal Screen Image
#### Schedule Tasks (Demonstrate Celery & Redis)
**(ppmvenv) D:\cidm6330>** curl -X POST http://127.0.0.1:8000/api/launch-tasks/

{"message":"10 tasks scheduled with 30-second intervals."}

![Terminal Screen Image](Celery_Task_Processing.jpg)

## Server Responses: Terminal Screen Image
![Terminal Screen Image](Server_Responses.jpg)

## Test Execution Results: Terminal Screen Image
![Terminal Screen Image](Test_Execution_Results.jpg)


# Python Code
All code files also available in the zip extract of the repository.

# References:
## Course Text:
Buelta, J. (2022). Python architecture patterns: Master API design, event-driven structures, and package management in Python. Packt Publishing.
https://www.amazon.com/Python-Architecture-Patterns-event-driven-structures/dp/1801819998

## Course References:
1. Tiangolo. (n.d.). FastAPI. FastAPI Documentation. Retrieved February 24, 2025, from https://fastapi.tiangolo.com/
2. Tiangolo. (n.d.). FastAPI reference. FastAPI Documentation. Retrieved February 24, 2025, from https://fastapi.tiangolo.com/reference/
3. Pydantic. (n.d.). Pydantic documentation. Retrieved February 27, 2025, from https://docs.pydantic.dev/latest/
4. Pydantic. (n.d.). BaseModel API. Pydantic Documentation. February 27, 2025, from https://docs.pydantic.dev/latest/api/base_model/
5. Fowler, M. (n.d.). TestDrivenDevelopment. MartinFowler.com. Retrieved April 11, 2025, from https://martinfowler.com/bliki/TestDrivenDevelopment.html
6. Cucumber. (n.d.). Behaviour-Driven Development. Retrieved April 8, 2025, from https://cucumber.io/docs/bdd/
7. Fowler, M. (2020, April 22). Domain Driven Design. MartinFowler.com. Retrieved April 8, 2025, from https://martinfowler.com/bliki/DomainDrivenDesign.html
8. Cucumber. (n.d.). Gherkin. Retrieved April 8, 2025, from https://cucumber.io/docs/gherkin/
9. Nowshin, A. (2023, October 25). How to do periodic tasks in a Django REST API using Celery and Redis? - A beginner-friendly guide. DEV Community. Retrieved April 10, 2025, from https://dev.to/afrozansenjuti/how-to-do-periodic-tasks-in-a-django-app-using-celery-and-redis-a-beginner-friendly-guide-3bp3

## Additional References:

1. Matthes, E. (2019). Python crash course: A hands-on, project-based introduction to programming (2nd ed.). No Starch Press. 
2. Richards, M., & Ford, N. (2020). Fundamentals of software architecture: An engineering approach. O'Reilly Media. 
3. Unhelkar, B. (2005). Software engineering with UML: Process, patterns, and applications. Auerbach Publications 
4. Dennis, A., Wixom, B. H., & Tegarden, D. (2020). Systems analysis and design: An object-oriented approach with UML (6th ed.). Wiley. 
5. Schulmeyer, G. G., & McManus, J. I. (1998). Handbook of software quality assurance (3rd ed.). Prentice Hall.
6. Golding, T. (2024). Building multi-tenant SaaS applications. O'Reilly Media.
7. Voron, F. (2023). Building data science applications with FastAPI - Second Edition: Develop, manage, and deploy efficient machine learning applications with Python. Packt Publishing.
8. Tiangolo, S. (2018). FastAPI: Fast (high-performance), web framework for building APIs with Python 3.6+. Retrieved from https://fastapi.tiangolo.com
9. Pydantic. (n.d.). Data validation and settings management using Python type hints. Retrieved from https://docs.pydantic.dev
10. Van Rossum, G., & Python Software Foundation. (2023). Python documentation: Data structures. Retrieved from https://docs.python.org/3/tutorial/datastructures.html
11. https://www.w3schools.com/python/pandas/default.asp 
12. The Pandas Development Team. (2023). pandas.DataFrame — pandas 2.0.3 documentation. Retrieved from https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
13. HogoNext. (n.d.). **How to create a DDD glossary**. Retrieved April 11, 2025, from https://hogonext.com/how-to-create-a-ddd-glossary/

