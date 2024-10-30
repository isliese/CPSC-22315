# Name : Chanran Kim
# Date : 11.09.24
# This file defines several functions which are managing contacts that we will use on main.py

# Define 'print_list' function
def print_list(contacts):

    print("\n================== CONTACT LIST ==================")
    print("Index   First Name            Last Name")
    print("======  ====================  ====================")
    
    for i in range(len(contacts)):
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')
    print("\n")


# Define 'add_contact' function
def add_contact(contacts, first_name="", last_name=""):
    # Add the contact
    a_contact = [first_name, last_name]
    contacts.append(a_contact)

    # return updated contact
    return contacts


# Define 'modify_contact' function
def modify_contact(contacts, first_name="", last_name="", index=""):
    index = int(index)

    # If the index it is not within the range of the contact list
    if index >= len(contacts):
        return False
    else: 
        # Modify the contact and return true
        a_contact = [first_name, last_name]
        contacts[index] = a_contact
        return True


# Define 'delete_contact' function
def delete_contact(contacts, index=""):
    index = int(index)

    # If the index it is not within the range of the contact list
    if index >= len(contacts):
        return False
    else: 
        # Delete the contact and return true
        contacts.pop(index)
        return True


# Define 'sort_contacts' function
def sort_contacts(contacts, column=""):
    column = int(column)  # convert the column to an integer
    contacts.sort(key=lambda x: x[column])  # sort the list in place
    return contacts
