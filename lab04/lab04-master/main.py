# Name : Chanran Kim
# Date : 18.09.24
# This program manages the contacts in many ways.
# You can print, add, modify and delete specific index depending on which acting you want to.

import contacts

# Define a variable to use for the contact list (dictionary format)
my_contacts = {}

# Implement a menu within a loop wi3th following choices
while True:
    print("\n     *** TUFFY TITAN CONTACT MAIN MENU\n")
    print("1. Add contact\n2. Modify contact\n3. Delete contact\n4. Print contact list\n5. Find contact\n6. Exit the program\n")
    
    menu_choice = input("Enter menu choice: ")

    # Perform action based on user choice

    # add_contact
    if menu_choice == '1':
        id = input("\nEnter phone number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")

        result = contacts.add_contact(my_contacts, id=id, first_name=first_name, last_name=last_name)
        # print result
        if result == 'error':
            print("Phone number already exists.")
        else:
            print(result)

    # modify_contact
    elif menu_choice == '2':
        id = input("\nEnter phone number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")

        result = contacts.modify_contact(my_contacts, id=id, first_name=first_name, last_name=last_name)
        # print result
        if result == 'error':
            print("Phone number does not exist.")
        else:
            print(result)

    # delete_contact
    elif menu_choice == '3':
        id = input("\nEnter phone number: ")

        result = contacts.delete_contact(my_contacts, id=id)
        # print result
        if result == 'error':
                print("Invalid phone number.")
        else:
            print(result)   

    # print contacts (sorted)
    elif menu_choice == '4':
        my_contacts = contacts.sort_contacts(my_contacts)
        contacts.print_list(my_contacts)

    # find contact
    elif menu_choice == '5':
        find = input("\nEnter search string: ")

        new_contacts = contacts.find_contact(my_contacts, find=find)
        
        # print found contacts
        print("================== FOUND CONTACT(S) ==================")
        print("Last Name             First Name            Phone")
        print("====================  ====================  ==========")
        
        for phone, contact in new_contacts.items():
            print(f'{contact[1]:22}{contact[0]:22}{phone:12}')
        print("\n")
        
    # exit 
    elif menu_choice == '6':
        break



