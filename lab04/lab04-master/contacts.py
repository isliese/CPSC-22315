# Name : Chanran Kim
# Date : 18.09.24
# This file defines several functions which are managing contacts that we will use on main.py

# Define 'print_list' function 
def print_list(contacts):

    print("\n==================== CONTACT LIST ====================")
    print("Last Name             First Name            Phone")
    print("====================  ====================  ==========")
    
    for phone, contact in contacts.items():
        print(f'{contact[1]:22}{contact[0]:22}{phone:12}')
    print("\n")



# Define 'add_contact' function
def add_contact(contacts, id="", first_name="", last_name=""):

    # If the id exists in the dictionary, return the string `error`
    if id in contacts:
        return 'error'
    else:
        # Add the contact
        a_contact = [first_name, last_name]
        contacts[id] = a_contact

        # Return the key:value pair that was added
        return "Added: " + first_name + " " + last_name + "."


# Define 'modify_contact' function
def modify_contact(contacts, id="", first_name="", last_name=""):

    # If the id does not exists in the dictionary, return the string `error`
    if not id in contacts:
        return 'error'
    else: 
        # Modify the contact 
        a_contact = [first_name, last_name]
        contacts[id] = a_contact

        # Return the key:value pair that was modified
        return "Modified: " + first_name + " " + last_name + "."


# Define 'delete_contact' function
def delete_contact(contacts, id=""):

    # If the id does not exists in the dictionary, return the string `error`
    if not id in contacts:
        return 'error'
    else: 
        first_name, last_name = contacts[id][0], contacts[id][1]
        
        # Remove and return the key:value pair with the key equal to id
        del contacts[id]
        return "Deleted: " + first_name + " " + last_name + "."


# Define 'sort_contacts' function
def sort_contacts(contacts):

    # Sort the dictionary in ascending order by last name, and then by first name, ignoring case.
    sorted_contacts = dict(sorted(contacts.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
    
    # Return the sorted dictionary
    return sorted_contacts


# Define 'find_contact' function
def find_contact(contacts, find=""):
    new_contacts = {}

    # Check if find is numeric
    if find.isdigit():
        find = int(find)
        if find in contacts:
            new_contacts[find] = contacts[find]
        return new_contacts

    # Check if find is a string
    find_lower = find.lower()
    for phone, contact in contacts.items():
        first_name, last_name = contact
        if find_lower in first_name.lower() or find_lower in last_name.lower():
            new_contacts[phone] = contact

    # Sort the created dictionary in ascending order by last name, and then by first name, ignoring case
    sorted_contacts = sort_contacts(new_contacts)

    return sorted_contacts

