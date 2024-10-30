import contacts

while True:
    print("*** TUFFY TITAN CONTACT MAIN MENU")
    print("1. Add contact\n2. Modify contact\n3. Delete contact\n4. Print contact list\n5. Set contact filename\n6. Exit the program")

    user_choice = int(input("Enter menu choice: "))

    # 1. Add contact
    if user_choice == 1:
        phone_number = input("Enter phone number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        name = contacts.add_contact(id=phone_number, first_name=first_name, last_name=last_name)
       
        print("Added: " + name)

    # 2. Modify contact
    if user_choice == 2:
        phone_number = input("Enter phone number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        name = contacts.modify_contact(id=phone_number, first_name=first_name, last_name=last_name)

        print("Modified: " + name)

    # 3. Delete contact
    if user_choice == 3:
        phone_number = input("Enter phone number: ")
        name = contacts.delete_contact(id=phone_number, first_name=first_name, last_name=last_name)

        print("Deleted: " + name)

    # 4. Print contact list
    if user_choice == 4:
        print("==================== CONTACT LIST ====================")
        print("Last Name             First Name            Phone")
        print("====================  ====================  ==========")

        for phone, contact in new_contacts.items():
            print(f'{contact[1]:22}{contact[0]:22}{phone:12}')
        print("\n")
    
    # 5. Set contact filename
    if user_choice == 5:
        continue

    # 6. Exit the program
    if user_choice == 6:
        break


