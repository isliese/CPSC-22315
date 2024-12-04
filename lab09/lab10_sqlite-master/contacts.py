# Name: Charnan Kim
# Date: 12/02/2024
# Contacts.py file

import sqlite3
import os

class Contacts:
    def __init__(self):
        # Class variable to store the database name
        self.database_name = ""

    def set_database_name(self, database_name):
        self.database_name = database_name
        # Check if the file exists; if not, create the database and tables
        if not os.path.exists(database_name):
            connection = sqlite3.connect(database_name) # connect
            cursor = connection.cursor()
            # Create the contacts table
            cursor.execute('''CREATE TABLE contacts (
                                contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                first_name TEXT,
                                last_name TEXT
                              )''')
            # Create the phones table
            cursor.execute('''CREATE TABLE phones (
                                phone_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                contact_id INTEGER,
                                phone_type TEXT,
                                phone_number TEXT,
                                FOREIGN KEY (contact_id) REFERENCES contacts (contact_id)
                              )''')
            connection.commit()
            connection.close()

    def get_database_name(self):
        return self.database_name

    def add_contact(self, first_name, last_name):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        # Insert a new contact
        cursor.execute('INSERT INTO contacts (first_name, last_name) VALUES (?, ?)', 
                       (first_name, last_name))
        connection.commit()
        connection.close()

    def modify_contact(self, contact_id, first_name, last_name):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        # Update contact information
        cursor.execute('UPDATE contacts SET first_name = ?, last_name = ? WHERE contact_id = ?', 
                       (first_name, last_name, contact_id))
        connection.commit()
        connection.close()

    def add_phone(self, contact_id, phone_type, phone_number):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        # Insert a new phone number for the contact
        cursor.execute('INSERT INTO phones (contact_id, phone_type, phone_number) VALUES (?, ?, ?)', 
                       (contact_id, phone_type, phone_number))
        connection.commit()
        connection.close()

    def modify_phone(self, phone_id, phone_type, phone_number):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        # Update phone information
        cursor.execute('UPDATE phones SET phone_type = ?, phone_number = ? WHERE phone_id = ?', 
                       (phone_type, phone_number, phone_id))
        connection.commit()
        connection.close()

    def get_contact_phone_list(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        # Query to get the contact list along with their phone numbers
        cursor.execute('''
            SELECT contacts.contact_id, contacts.first_name, contacts.last_name, 
                   phones.phone_id, phones.contact_id, phones.phone_type, phones.phone_number
            FROM contacts 
            LEFT JOIN phones ON contacts.contact_id = phones.contact_id
        ''')
        result = cursor.fetchall()
        connection.close()
        return result
