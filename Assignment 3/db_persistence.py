
"""
Script Name: [db_persistence.py]
Author: David H. Slack
Copyright: @ 2025, David H. Slack
Date Created: 2025.03.15
Last Modified: 2025.03.15
Version: 1.0.0.0000
	
Description: 
	The db_persistence.py module provides the SQLite-based storage system for
    managing contact records. It provides the interaction with a MySQL database.

References:
https://sqlitebrowser.org/

Note:
    Switched to SQLite from MySQL per examples in course materials and lecture.

"""

# =============================================
# Import necessary modules
# =============================================
# Import the os and sys modules, even if they may not used they
# are included as part of my normal python template.
import os
import sys

# Additional imports here
from fastapi import FastAPI # Import FastAPI to create the web application.
from fastapi import HTTPException # Import HTTPException to handle HTTP errors.
from pydantic import BaseModel # Import Pydantic's model for request/response validation.
from datetime import date # Import date to handle member date of birth (DOB) fields.
from typing import List # Import List for type hinting when returning a list of members.
import sqlite3 # Import the SQLite3 module for interacting with a SQLite database.


# The class for managing contact records using SQLite database.
class SQLitePersistence:

    # SQLite connection, creates the table if it does not exist.
    def __init__(self, db_path="contacts.db"):

        self.db_path = db_path
        self.initialize_db()  # Ensure the database, table, and contacts exist.
        self.connection = sqlite3.connect(self.db_path, check_same_thread=False) # Make the connection.
        """
        Added: check_same_thread=False to connection.
        This Stack overflow question (post) resolved an error in my code regarding
        this error: 

            sqlite3.ProgrammingError: SQLite objects created in a thread can only 
            be used in that same thread. The object was created in thread id 29404
            and this is thread id 38672.
        
        Stack Overflow User. (2018, January 12). Objects created in a thread can 
        only be used in that same thread [Online forum post]. Stack Overflow. 
        Retrieved from https://stackoverflow.com/questions/48218065/objects-created-in-a-thread-can-only-be-used-in-that-same-thread
        """

        self.connection.row_factory = sqlite3.Row  # Enables dictionary-like access to rows.
        self.cursor = self.connection.cursor() 
       

    def initialize_db(self):
         # Check if the database file exists, create it if not.
        db_exists = os.path.exists(self.db_path)

        # Connect to SQLite and create the db file if it does not exist.
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        if not db_exists:
            print("Database and table not found, created successfully.")

        # Create 'contact' table if it does not exist. It shouldn't at first run.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contact (
                Contact_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                First_Name TEXT NOT NULL,
                Last_Name TEXT NOT NULL,
                Phone TEXT NOT NULL,
                Applicant_Relationship TEXT NOT NULL
            )
        """)
        connection.commit()

        # Check if the first 10 contacts exist, if not add them.
        cursor.execute("SELECT COUNT(*) FROM contact")
        count = cursor.fetchone()[0]

        if count < 10:
            print("Inserting default contacts as defined in db_persistence.py")
            self.insert_default_contacts(cursor, connection)

        connection.commit()
        connection.close()


    # Insert the first 10 contacts when they do not exist.
    def insert_default_contacts(self, cursor, connection):

        contacts = [
            ("Alice", "Johnson", "555-123-4567", "Parent"),
            ("Bob", "Smith", "555-234-5678", "Guardian"),
            ("Charlie", "Brown", "555-345-6789", "Sibling"),
            ("Diana", "King", "555-456-7890", "Spouse"),
            ("Edward", "White", "555-567-8901", "Parent"),
            ("Fiona", "Adams", "555-678-9012", "Guardian"),
            ("George", "Hill", "555-789-0123", "Sibling"),
            ("Hannah", "Scott", "555-890-1234", "Parent"),
            ("Isaac", "Thomas", "555-901-2345", "Guardian"),
            ("Julia", "Martin", "555-012-3456", "Spouse"),
        ]
        
        cursor.executemany(
            "INSERT INTO contact (First_Name, Last_Name, Phone, Applicant_Relationship) VALUES (?, ?, ?, ?)",
            contacts
        )
        print("Default contacts not found in db, inserted successfully.")



# =============================================
# Create, Read, Update, Delete (CRUD) methods as:
# list (all), create, read, update, delete, for consistency.
# =============================================

    # Get all contact records in the database in the contacts table.
    def list_contacts(self):
 
        self.cursor.execute("SELECT * FROM contact")  # Select all records.
        results = self.cursor.fetchall()  # Fetch result.

        if not results:
            # This shouldn't happen if the code above for the checks functions correctly.
            raise HTTPException(status_code = 404, detail = "No contacts found in the database. Crumbs!")

        return [dict(row) for row in results]  # Convert rows to list.


    # Create a new contact record.
    def create_contact(self, contact: dict):

        sql = "INSERT INTO contact (First_Name, Last_Name, Phone, Applicant_Relationship) VALUES (?, ?, ?, ?)"
        self.cursor.execute(sql, (contact["First_Name"], contact["Last_Name"], contact["Phone"], contact["Applicant_Relationship"]))
        self.connection.commit()

        # Get the last inserted ID.
        contact["Contact_ID"] = self.cursor.lastrowid
        return contact


    # Get a contact record by Contact_ID.
    def read_contact(self, contact_id: int):
 
        self.cursor.execute("SELECT * FROM contact WHERE Contact_ID = ?", (contact_id,))
        result = self.cursor.fetchone()

        if not result:
            raise HTTPException(status_code = 404, detail = "Contact not found, are you sure you have records!")

        return dict(result)


    # Update an existing contact by Contact_ID.
    def update_contact(self, contact_id: int, updated_contact: dict):

        sql = "UPDATE contact SET First_Name = ?, Last_Name = ?, Phone = ?, Applicant_Relationship = ? WHERE Contact_ID = ?"
        self.cursor.execute(sql, (updated_contact["First_Name"], updated_contact["Last_Name"], updated_contact["Phone"], updated_contact["Applicant_Relationship"], contact_id))
        self.connection.commit()

        if self.cursor.rowcount == 0:
            raise HTTPException(status_code = 404, detail = "Contact not found")

        return updated_contact


    # Delete a contact by Contact_ID.
    def delete_contact(self, contact_id: int):

        self.cursor.execute("DELETE FROM contact WHERE Contact_ID = ?", (contact_id,))
        self.connection.commit()

        if self.cursor.rowcount == 0:
            raise HTTPException(status_code = 404, detail = "Contact not found")

        return {"delete_contact": "Contact deleted"}