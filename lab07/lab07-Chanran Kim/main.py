import contacts

# Create an instance of the Contacts class
contact_list = contacts.Contacts()  # Optionally, add a filename if you want to load/save to a file

while True:
    print("\n*** TUFFY TITAN CONTACT MAIN MENU")
    print("1. Add contact\n2. Modify contact\n3. Delete contact\n4. Print contact list\n5. Set contact filename\n6. Exit the program")

    user_choice = int(input("\nEnter menu choice: "))

    # 1. Add contact
    if user_choice == 1:
        phone_number = input("Enter phone number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        name = contact_list.add_contact(id=phone_number, first_name=first_name, last_name=last_name)
       
        print("\nAdded: " + fisrt_name, last_name)

    # 2. Modify contact
    if user_choice == 2:
        phone_number = input("Enter phone number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        name = contact_list.modify_contact(id=phone_number, first_name=first_name, last_name=last_name)

        print("\nModified: " + name)

    # 3. Delete contact
    if user_choice == 3:
        phone_number = input("Enter phone number: ")
        name = contact_list.delete_contact(id=phone_number)

        print("\nDeleted: " + name)

    # 4. Print contact list
    if user_choice == 4:
        print("==================== CONTACT LIST ====================")
        print("Last Name             First Name            Phone")
        print("====================  ====================  ==========")

        for phone, contact in contact_list.data.items():
            print(f'{contact[1]:22}{contact[0]:22}{phone:12}')
        print("\n")
    
    # 5. Set contact filename
    if user_choice == 5:
        filename = input("Enter filename to save contacts: ")
        contact_list.filename = filename

    # 6. Exit the program
    if user_choice == 6:
        break
