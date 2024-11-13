# Name : Chanran Kim 
# Date : 10/18/2024

import json

# A class named 'Contacts'
class Contacts: 
    
    # __init__ function
    def __init__(self, filename=None):
        self.filename = filename
        self.data = {}

        if filename:
            try:
                with open(filename, 'r') as file:
                    self.data = json.load(file)
            except FileNotFoundError:
                print(f"File '{filename}' not found.")


    # add_contact function
    def add_contact(self, id=None, first_name=None, last_name=None):
        if id in self.data:
            return "Phone number already exists."
        
        self.data[id] = [first_name, last_name]
        
        # Sort the data dictionary by last name, then by first name, ignoring case
        self.data = dict(sorted(self.data.items(), key=lambda x: (x[1][1].lower(), x[1][0].lower())))
        
        # Write the updated data dictionary to the file
        if self.filename:
            with open(self.filename, 'w') as file:
                json.dump(self.data, file, indent=4)

        name = first_name + last_name
        return name


    # modify_contact function
    def modify_contact(self, id=None, first_name=None, last_name=None):
        if id not in self.data:
            return "error"
        
        self.data[id] = [first_name, last_name]

        # Sort the data dictionary by last name, then by first name, ignoring case
        self.data = dict(sorted(self.data.items(), key=lambda x: (x[1][1].lower(), x[1][0].lower())))

        # Write the updated data dictionary to the file
        if self.filename:
            with open(self.filename, 'w') as file:
                json.dump(self.data, file, indent=4)

        name = first_name + last_name
        return name


    # delete_contact function
    def delete_contact(self, id=None):
        if id not in self.data:
            return "Invalid phone number."
        
        # save name that will be deleted
        name = self.data[id][0] + self.data[id][1]
        
        # Remove the key:value pair with the key equal to id.
        del self.data[id]

        # Write the updated data dictionary to the file
        if self.filename:
            with open(self.filename, 'w') as file:
                json.dump(self.data, file, indent=4)

        return name
