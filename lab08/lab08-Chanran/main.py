# Name : Chanran Kim 
# Date : 11/05/2024

from people import Faculty
from people import Student

faculty_list = []
student_list = []

while True:
    print("\n*** TUFFY TITAN STUDENT/FACULTY MAIN MENU")
    print("1. Add faculty\n2. Print faculty\n3. Add student\n4. Print student\n9. Exit the program")

    try:
        user_choice = int(input("Enter menu choice: "))
    except ValueError:
        print("Invalid input. Please enter a number from the menu options.")
        continue

    # 1. Add faculty
    if user_choice == 1:
        firstname = input("Enter first name: ")
        lastname = input("Enter last name: ")
        department = input("Enter department: ")
        faculty = Faculty(firstname, lastname, department)
        faculty_list.append(faculty)


    # 2. Print faculty
    elif user_choice == 2:
        if not faculty_list:
            print("No faculty members available.")
        else:
            print("\n==================== FACULTY LIST ====================")
            print(f"{'Last Name':<20} {'First Name':<20} {'Department':<20}")
            print("=====================================================")
            for faculty in faculty_list:
                print(f"{faculty.lastname:<20} {faculty.firstname:<20} {faculty.department:<20}")

    # 3. Add student
    elif user_choice == 3:
        firstname = input("Enter first name: ")
        lastname = input("Enter last name: ")
        classyear = input("Enter class year: ")
        major = input("Enter major: ")
        advisor_firstname = input("Enter advisor's first name: ")
        advisor_lastname = input("Enter advisor's last name: ")
        advisor_department = input("Enter advisor's department: ")

        # Create the advisor as a Faculty member
        advisor = Faculty(advisor_firstname, advisor_lastname, advisor_department)

        # Create the student and set their details
        student = Student(firstname, lastname)
        student.set_class(classyear)
        student.set_major(major)
        student.set_advisor(advisor)
        student_list.append(student)

    # 4. Print student
    elif user_choice == 4:
        if not student_list:
            print("No students available.")
        else:
            print("\n==================== STUDENT LIST ====================")
            print(f"{'Last Name':<20} {'First Name':<20} {'Class Year':<20} {'Major':<20} {'Advisor':<20}")
            print("=====================================================================")
            for student in student_list:
                advisor_name = f"{student.advisor.firstname} {student.advisor.lastname}"
                print(f"{student.lastname:<20} {student.firstname:<20} {student.classyear:<20} {student.major:<20} {advisor_name:<20}")

    # 9. Exit the program
    elif user_choice == 9:
        print("Exiting the program...")
        break

    else:
        print("Invalid menu choice. Please select a valid option.")
