
"""
Script Name: [csv_persistence.py]
Author: David H. Slack
Copyright: @ 2025, David H. Slack
Date Created: 2025.03.15
Last Modified: 2025.03.15
Version: 1.0.0.0000
	
Description: 
	The csv_persistence.py module provides the flat-file CSV-based storage 
    system to manage address records. The persistence provides storing, 
    retrieving, updating, and deleting address information in a CSV file.
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
import pandas as pd # Import Pandas for CSV file manipulation

app = FastAPI()

# Define the csv file location (path).
CSV_FILE = "address.csv"

# Define the csv column headers.
COLUMNS = [
    "Address_ID",  # Unique identifier for each address (Primary Key).
    "Street_No",  # House number.
    "Street",  # Street name.
    "City",  # City of the address.
    "State", # State of the address.
    "Zip",  # Zip code of the address.
    "Type",  # Address type classification (Home, Work, etc.).
    "OwnerID",  # Contact owner identifier (Foreign Key to Contact entity).
    "OwnerType",  # Owner type classification (Self, Parent, Guardian, etc.).
]


# The class for managing address records using the csv file.
class CSVPersistence:

    # If the file does not exist, create a new one with headers.
    # Watch it... the 1st attempt created an empty file by mistake!
    # Drop the use of subfolders for now!
    def __init__(self, file_path=CSV_FILE):

        self.file_path = file_path
        if not os.path.exists(self.file_path):
            df = pd.DataFrame(columns=COLUMNS)
            df.to_csv(self.file_path, index=False)

    # Load the file.
    def _load_data(self):
        return pd.read_csv(self.file_path)

    # Need to read more on dataframe concepts.
    # https://www.geeksforgeeks.org/python-pandas-dataframe/
    def _save_data(self, df):
        df.to_csv(self.file_path, index=False)



# =============================================
# Create, Read, Update, Delete (CRUD) methods as:
# list (all), create, read, update, delete, for consistency.
# =============================================


    # Get all addresses in the csv file.
    def list_addresses(self):
        df = self._load_data()  # Load data from the csv file.

        if df.empty:
            raise HTTPException(status_code = 404, detail = "No addresses found.")

        return df.to_dict(orient="records")


    # Create a new address.
    def create_address(self, address: dict):
        df = self._load_data()

        # Generate a unique Address_ID
        # Find the current max ID and increment for tha new one.
        address_id = df["Address_ID"].max() + 1 if not df.empty else 1
        address["Address_ID"] = address_id

        # Append (concat) the new address
        # Per:
        # Stack Overflow User. (2023, April 7). Error: DataFrame object has no 
        # attribute 'append' [Online forum post]. Stack Overflow. Retrieved from
        # https://stackoverflow.com/questions/75956209/error-dataframe-object-has-no-attribute-append
        df = df.concat(address, ignore_index=True)
        self._save_data(df)

        # return address
        return {"create_address": "The address was created.", "address": address}


    # Get an address by ID.
    def read_address(self, address_id: int):
        df = self._load_data()
        record = df[df["Address_ID"] == address_id]

        # Error if not a valid address_id.
        if record.empty:
            raise HTTPException(status_code = 404, detail = "Address ID was not found. Confirm ID.")

        return record.to_dict(orient="records")[0]

    # Update an address.
    def update_address(self, address_id: int, updated_address: dict):
        df = self._load_data()

        # Confirm provided address id is valid.
        if address_id not in df["Address_ID"].values:
            raise HTTPException(status_code = 404, detail = "Address ID was not found.")

        # Update the address record
        df.loc[df["Address_ID"] == address_id, list(updated_address.keys())] = list(updated_address.values())
        self._save_data(df)

        return {"update_address": "The address was updated successfully.", "updated_address": updated_address}



    # Delete an address. 
    # Ensure a backup of the file prior to testing!
    def delete_address(self, address_id: int):
        df = self._load_data()

        if address_id not in df["Address_ID"].values:
            raise HTTPException(status_code = 404, detail = "Address ID was not found. Confirm ID")

        # Remove the address from csv file.
        df = df[df["Address_ID"] != address_id]
        self._save_data(df)

        return {"delete_address": "Address deleted"}
