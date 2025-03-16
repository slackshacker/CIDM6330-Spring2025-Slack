
"""
Script Name: [in_memory_persistence.py]
Author: David H. Slack
Copyright: @ 2025, David H. Slack
Date Created: 2025.03.14
Last Modified: 2025.03.14
Version: 1.0.0.0000
	
Description: 
	The in_memory_persistence.py module for the in-memory data storage to manage
    applicant records. The persistence is designed to allow temporary data 
    storage, meaning that all records will be lost when the application restarts. 
"""

# =============================================
# Import necessary modules
# =============================================
# Import the os and sys modules, even if they may not used they
# are included as part of my normal python template.
# import os
# import sys

# Additional imports here
from fastapi import FastAPI # Import FastAPI to create the web application.
from fastapi import HTTPException # Import HTTPException to handle HTTP errors.
from pydantic import BaseModel # Import Pydantic's model for request/response validation.
from datetime import date # Import date to handle member date of birth (DOB) fields.
from typing import List # Import List for type hinting when returning a list of members.

app = FastAPI()

class InMemoryPersistence:

    # Initializes the in-memory database for applicants.
    def __init__(self):
 
        self.applicants = {}  # Dictionary to store applicants in memory
        self.current_id = 1   # Set the counter for the first Applicant_ID

        # Predefined members, with 10 initial members.
        # https://www.analyticsvidhya.com/blog/2024/02/how-to-create-a-list-of-dictionaries-in-python/
        members = [
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

        # Load the initial applicants.
        for member in members:
            member["Applicant_ID"] = self.current_id  # Assign a unique Applicant_ID.
            self.applicants[self.current_id] = member  # Store applicant in dictionary.
            self.current_id += 1 # At the end of the load this should be set to 11.



# =============================================
# Create, Read, Update, Delete (CRUD) methods as:
# list (all), create, read, update, delete, for consistency.
# =============================================


    # Get a list of all the applicants.
    def list_applicants(self):
 
        if not self.applicants:
            raise HTTPException(status_code = 404, detail = "No applicants found in memory!")

        return list(self.applicants.values())  # Return all applicants as a list of dictionaries


    # Create a new applicant.
    def create_applicant(self, applicant: dict):
        
        applicant["Applicant_ID"] = self.current_id # Should be set to 11 for 1st create.
        self.applicants[self.current_id] = applicant
        self.current_id += 1

        return {"create_applicant": "The applicant was created.", "applicant": applicant}


    # Get an applicant by their ID.
    def read_applicant(self, applicant_id: int):
        
        if applicant_id in self.applicants:
            return self.applicants[applicant_id]
        
        raise HTTPException(status_code = 404, detail = "Applicant ID was not found.")


    # Update an existing applicant details.
    def update_applicant(self, applicant_id: int, updated_applicant: dict):
       
        if applicant_id in self.applicants:
            updated_applicant["Applicant_ID"] = applicant_id
            self.applicants[applicant_id] = updated_applicant
            
            return {"update_applicant": "The applicant was updated.", "applicant": updated_applicant}
        
        raise HTTPException(status_code = 404, detail = "Applicant ID was not found.")


    # Delete an applicant by their ID.
    def delete_applicant(self, applicant_id: int):
 
        if applicant_id in self.applicants:
            del self.applicants[applicant_id]

            return {"delete_applicant": "Applicant deleted."}
        
        raise HTTPException(status_code = 404, detail = "Applicant ID was not found.")
