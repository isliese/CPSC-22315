# Name : Chanran Kim
# Date : 11.09.24
# This program manages the contacts in many ways.
# You can print, add, modify and delete specific index depending on which acting you want to.

import contacts

# Define a variable to use for the contact list
my_contacts = []

# Implement a menu within a loop wi3th following choices
while True:
    print("\n     *** TUFFY TITAN CONTACT MAIN MENU\n")
    print("1. Print list\n2. Add contact\n3. Modify contact\n4. Delete contact\n5. Sort list by first name\n6. Sort list by last name\n7. Exit the program\n")
    print("Please choose a number to act or exit.\n")
    
    menu_choice = input("Enter menu choice: ")

    # Perform action based on user choice

    # print_list
    if menu_choice == '1':
        contacts.print_list(my_contacts)

    # add_contact
    elif menu_choice == '2':
        first_name = input("\nEnter first name: ")
        last_name = input("Enter last name: ")
        my_contacts = contacts.add_contact(my_contacts, first_name=first_name, last_name=last_name)

    # modify_contact
    elif menu_choice == '3':
        index = input("\nEnter the index number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        success = contacts.modify_contact(my_contacts, first_name=first_name, last_name=last_name, index=index)
        if not success:
            print("Invalid index number.")

    # delete_contact
    elif menu_choice == '4':
        index = input("\nEnter the index number: ")
        success = contacts.delete_contact(my_contacts, index=index)
        if not success:
            print("Invalid index number.")
    
    # sort_contacts by first name
    elif menu_choice == '5':
        column = 0
        my_contacts = contacts.sort_contacts(my_contacts, column=column)
    
    # sort_contacts by last name
    elif menu_choice == '6':
        column = 1
        my_contacts = contacts.sort_contacts(my_contacts, column=column)

    # exit 
    elif menu_choice == '7':
        break




