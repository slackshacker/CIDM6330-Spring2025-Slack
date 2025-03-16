"""
Script Name: [main.py]
Author: David H. Slack
Copyright: @ 2025, David H. Slack
Date Created: 2025.03.14
Last Modified: 2025.03.14
Version: 1.0.0.0000
	
Description: 
		Creates an API using Python and FastAPI for the CIDM 6330 - Assignment 
        03, Extend Your API with a Repository Deliverables. This API is designed
        to support the course project's Entity-Relationship Diagram (ERD) by 
        implementing three instantiation contexts for the API:

            1.	SQLModel Repository
            2.	CSV Repository
            3.	In-Memory Repository
		
Instructor course notes:
    The result of your work should closely mirror what you see in the SQLModel
    "Heros" FastAPI/Pydantic tutorial. 

    API CRUD + Repository Persistence
    The purpose of this assignment is to have a full API + Persistence means of
    simple state changes for your system. Note that there is no business logic
    present as of yet, we are simply facilitating CRUD operations for API + 
    Respository-driven persistence

References:
    1. Tiangolo, S. (2018). FastAPI: Fast (high-performance), web framework for 
       building APIs with Python 3.6+. Retrieved from https://fastapi.tiangolo.com
    2. Pydantic. (n.d.). Data validation and settings management using Python type 
       hints. Retrieved from https://docs.pydantic.dev
    3. Van Rossum, G., & Python Software Foundation. (2023). Python documentation: 
       Data structures. Retrieved from 
       https://docs.python.org/3/tutorial/datastructures.html
    4. https://www.w3schools.com/python/pandas/default.asp
    5. The Pandas Development Team. (2023). pandas.DataFrame — pandas 2.0.3 
       documentation. Retrieved from https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

Course reference & example: 
    https://github.com/ahuimanu/CIDM6330/blob/SPRING2025/CIDM6330-Spring2025/Evolution_02_Repository/2025/main.py
    https://github.com/ahuimanu/CIDM6330/blob/SPRING2025/CIDM6330-Spring2025/Evolution_02_Repository/2025/generic.py
    https://github.com/ahuimanu/CIDM6330/blob/SPRING2025/CIDM6330-Spring2025/Evolution_02_Repository/2025/repository.py

Access API documentation:
    Open Swagger UI: http://127.0.0.1:8000/docs
    Open Redoc UI: http://127.0.0.1:8000/redoc
"""

# =============================================
# Import necessary modules
# =============================================
# Import the os and sys modules.
import os # May not be used, import anyway.
import sys # May not be used, import anyway.

# Additional imports here
from datetime import date  # Needed for DOB handling
from pydantic import BaseModel  # Model validation
from fastapi import HTTPException  # Error handling
from fastapi import FastAPI  # Web framework
from typing import List  # List typing 

# Using individual files for each repository type.
# Import the InMemoryPersistence class from the in_memory_persistence.py (Applicant)
from in_memory_persistence import InMemoryPersistence 

# Import the CSVPersistence class from csv_persistence.py (Address)
from csv_persistence import CSVPersistence

 # Import the SQLitePersistence class from mysql_persistence.py (Contact) 
 # Using SQLite due to course examples. 
from db_persistence import SQLitePersistence


app = FastAPI()

# Initialize the persistence layers.
in_memory_db = InMemoryPersistence()
csv_db = CSVPersistence("address.csv")
sqlite_db = SQLitePersistence()


# =============================================
# Establish the API Endpoints (routes).
# =============================================
# Reference: FastAPI. (n.d.). First Steps. FastAPI. Retrieved March 1, 2025, from https://fastapi.tiangolo.com/tutorial/first-steps/

# Set the root messaging for the project.
# =============================================
@app.get("/")
def project_intro():
    return {"CIDM 6330 - Assignment 03": "Extend Your API with a Repository"} # The project title


# =============================================
# Create, Read, Update, Delete (CRUD) methods as:
# list (all), create, read, update, delete, for consistency.
# =============================================

# In-Memory Persistence (Applicant).
# =============================================

# Get all applicants.
# https://swagger.io/specification/?sbsearch=route%20summary, used here after.
@app.get("/applicants", 
         summary="List all applicants stored in-memory.", 
         description="Retrieves a list of applicants. Data resets when the server restarts!")
def list_applicants():
    applicants = in_memory_db.list_applicants()

    if not applicants:
        return {"get_all_applicants error:": "No applicants found."}

    return {"applicants": applicants}


# Create a new applicant.
@app.post("/applicant/")
def create_applicant(applicant: dict):
    result = in_memory_db.create_applicant(applicant) 

    return {"create_applicant": "New applicant added.", "data": result}


# Retrieve an applicant's details.
@app.get("/applicant/{applicant_id}")
def read_applicant(applicant_id: int):
    applicant = in_memory_db.read_applicant(applicant_id)

    if not applicant:
        # https://docs.python.org/3/library/string.html#custom-string-formatting, used here after.
        return {"get_applicant error": "Sorry, can not find an applicant with ID {}.".format(applicant_id)}

    return {"applicant": applicant}


# Update an existing applicant's data
@app.put("/applicant/{applicant_id}")
def update_applicant(applicant_id: int, applicant: dict):
    updated_applicant = in_memory_db.update_applicant(applicant_id, applicant)

    # If applicant ID does not exist
    if not updated_applicant:
        return {"update_applicant error:": "Could not find the applicant with ID {}.".format(applicant_id)}

    return {"update_applicant": "Applicant updated successfully.", "data": updated_applicant}

# Delete an applicant.
@app.delete("/applicant/{applicant_id}")
def delete_applicant(applicant_id: int):
    deleted = in_memory_db.delete_applicant(applicant_id)

    # If applicant ID does not exist
    if not deleted:
        return {"delete_applicant error:": "Could not find the applicant with ID {}.".format(applicant_id)}

    return {"deleted_applicant": "Applicant {} deleted successfully.".format(applicant_id)}



# CSV Persistence (Address).
# =============================================

# Get all addresses from the csv file.
# https://swagger.io/specification/?sbsearch=route%20summary, used here after.
@app.get("/addresses", 
         summary="Retrieve all addresses.", 
         description="Returns a full list of stored addresses from the CSV file.")
def list_addresses():
    addresses = csv_db.list_addresses()

    # If no addresses exist.
    if not addresses:
        return {"get_all_addresses error:": "No addresses found. Check the csv file."}

    return {"addresses": addresses}


# Add a new address to the csv file.
@app.post("/address/")
def create_address(address: dict):
    result = csv_db.create_address(address)
    return {"create_address error:": "Address successfully added to csv file.", "data": result}


# Get a specific address by its ID from the csv file.
@app.get("/address/{address_id}")
def read_address(address_id: int):
    address = csv_db.read_address(address_id)
    if not address:
        return {"get_address error:": "Couldn not find the address with ID {}.".format(address_id)}

    return {"address": address}


# Update an existing address in the csv file.
@app.put("/address/{address_id}")
def update_address(address_id: int, address: dict):
    updated_address = csv_db.update_address(address_id, address)
    if not updated_address:
        return {"update_address error:": "No address found with ID {}. Update failed.".format(address_id)}

    return {"update_address": "Address updated successfully.", "data": updated_address}


# Delete an address from the CSV database
@app.delete("/address/{address_id}")
def delete_address(address_id: int):
    deleted = csv_db.delete_address(address_id)
    if not deleted:
        return {"delete_address error:": "Address ID {} was not found. Check the ID.".format(address_id)}

    return {"delete_address": "Address with ID {} deleted.".format(address_id)}



# SQLite Persistence (Contact).
# =============================================

# Get a list of all contacts currently in the database.
# https://swagger.io/specification/?sbsearch=route%20summary, used here after.
@app.get("/contacts", response_model=list, 
         summary="Get a list of all contacts currently in the database.", 
         description="Retrieve all contact records from the database.")
def list_contacts():
    contact = sqlite_db.list_contacts()
    if not contact:
        return {"list_contacts error:": "Contacts not found!"}
    
    return contact


# Create a new contact in the database.
@app.post("/contact/")
def create_contact(contact: dict):
    new_contact = sqlite_db.create_contact(contact)

    return {"create_contact": "New contact added.", "data": new_contact}


# Retrieve a contact by ID from the database.
@app.get("/contact/{contact_id}")
def read_contact(contact_id: int):
    contact = sqlite_db.read_contact(contact_id)

    if not contact:
        return {"get_contact error:": "Contact not found with ID {}. Check the database.".format(contact_id)}

    return {"contact": contact}


# Update an existing contact in the database.
@app.put("/contact/{contact_id}")
def update_contact(contact_id: int, contact: dict):
    updated_contact = sqlite_db.update_contact(contact_id, contact)

    # If contact doesn't exist in the database.
    if not updated_contact:
        return {"update_contact error:": "No contact found with ID {}. No update.".format(contact_id)}

    return {"update_contact": "Contact updated successfully.", "data": updated_contact}


# Delete a contact from the database.
@app.delete("/contact/{contact_id}")
def delete_contact(contact_id: int):
    deleted = sqlite_db.delete_contact(contact_id)

    if not deleted:
        return {"delete_contact error:": "Contact with ID {} not found.".format(contact_id)}

    return {"delete_contact": "Contact with ID {} deleted.".format(contact_id)}