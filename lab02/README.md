# Laboratory 2

## Laboratory Objectives
1. Explore and use various tools such as: GitHub, VirtualBox, Tuffix, Linux Terminal, and VS Code.
1. Write a Python program using:
     1. lists
     2. loops
     3. conditional statements
     4. input/output
     5. modules
     6. functions
1. Run and test a Python program.

## Getting Started

1. Setting Up Python Environment

     - Verify Python Installation:
     - Open your terminal (Command Prompt for Windows, Terminal for macOS/Linux).
     - Type python --version and press Enter.
     - You should see the installed Python version displayed.

2. Configuring Visual Studio Code (VS Code)

     - Install Python Extension:
     - Open VS Code.
     - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing Ctrl+Shift+X.
     - Search for “Python” in the Extensions Marketplace.
     - Click “Install” on the Python extension by Microsoft.

3. Running Python in VS Code

     - Create a New Python File:
     - In VS Code, open a folder where you want to save your Python projects.
     - Click on File > New File or press Ctrl+N to create a new file.
     - Save the file with a .py extension (e.g., hello.py).
     
## Program Instructions
1. Write a Python program that performs as a Tuffy Titan Contact List which contains a list of contacts that can be modified or deleted.

1. Create a `contacts` module to meet the following requirements:
     1. Create a file named `contacts.py`.
     1. Add a comment at the top of the file which indicates your name, date and the purpose of the file.
     2. Note: All contact lists within this module should assume the list is of the form: `[["first name","last name"],["first name","last name"],...]`
     3. Define a function named `print_list` to meet the following requirements:
          1. Take a contact list as a parameter.
          2. Implement a docstring with a simple sentence that describes the function.
          3. Print a header for the printout which indicates the list index number, the first name, and the last name column headers.
          4. Loop through the contact list and print each contact on a separate line displaying: the list index number, the contact first name, and the contact last name.  Assuming `i` is the index value and `contacts` is the name of the list, the following will format the output: `print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')`
     4. Define a function named `add_contact` to meet the following requirements:
          1. Take a contact list as a parameter.
          2. Implement a docstring with a simple sentence that describes the function.
          3. Prompt the user for the first name.
          4. Prompt the user for the last name.
          5. Add the contact to the list.
          6. Return the updated list.
     5. Define a function named `modify_contact` to meet the following requirements:
          1. Take a contact list as a parameter.
          2. Implement a docstring with a simple sentence that describes the function.
          3. Prompt the user for the list index number to modify. If the index it is not within the range of the contact list, print out `Invalid index number.` and return the unedited list.
          4. Prompt the user for the first name.
          5. Prompt the user for the last name.
          6. Modify the contact list at the index value.
          7. Return the updated list.
     6. Define a function named `delete_contact` to meet the following requirements:
          1. Take a contact list as a parameter.
          2. Implement a docstring with a simple sentence that describes the function.
          3. Prompt the user for the list index number to delete. If the index it is not within the range of the contact list, print out `Invalid index number.` and return the unedited list.
          5. Delete the contact at the index value.
          6. Return the updated list.
1. Create a `main` driver program to meet the following requirements:
     1. Create a file named `main.py`.
     1. Add a comment at the top of the file which indicates your name, date and the purpose of the file.
     1. Import the `contacts` module.
     2. Define a variable to use for the contact list. 
     3. Implement a menu within a loop with following choices:
          1. Print list
          2. Add contact
          3. Modify contact
          4. Delete contact
          5. Exit the program
     4. Prompt the user for the menu choice and call the appropriate `contacts` function or exit the program.

1. Run the program using the command below and repeat the steps above until you are satisfied your program output meets the above requirements.

    ```
    python3 -m main
    ```


1. Typical input and output for the program:
     ```
           *** TUFFY TITAN CONTACT MAIN MENU

     1. Print list
     2. Add contact
     3. Modify contact
     4. Delete contact
     5. Exit the program

     Enter menu choice: 2

     Enter first name: Richard
     Enter last name: Stallman

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Print list
     2. Add contact
     3. Modify contact
     4. Delete contact
     5. Exit the program

     Enter menu choice: 2

     Enter first name: Bill
     Enter last name: Gates

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Print list
     2. Add contact
     3. Modify contact
     4. Delete contact
     5. Exit the program

     Enter menu choice: 2

     Enter first name: Steve
     Enter last name: Jobs

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Print list
     2. Add contact
     3. Modify contact
     4. Delete contact
     5. Exit the program

     Enter menu choice: 1

     ================== CONTACT LIST ==================
     Index   First Name            Last Name
     ======  ====================  ====================
     0       Richard               Stallman              
     1       Bill                  Gates                 
     2       Steve                 Jobs                  

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Print list
     2. Add contact
     3. Modify contact
     4. Delete contact
     5. Exit the program

     Enter menu choice: 3

     Enter the index number: 2
     Enter first name: Tim
     Enter last name: Cook

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Print list
     2. Add contact
     3. Modify contact
     4. Delete contact
     5. Exit the program

     Enter menu choice: 1

     ================== CONTACT LIST ==================
     Index   First Name            Last Name
     ======  ====================  ====================
     0       Richard               Stallman              
     1       Bill                  Gates                 
     2       Tim                   Cook                  

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Print list
     2. Add contact
     3. Modify contact
     4. Delete contact
     5. Exit the program

     Enter menu choice: 3

     Enter the index number: 5
     Invalid index number.

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Print list
     2. Add contact
     3. Modify contact
     4. Delete contact
     5. Exit the program

     Enter menu choice: 4

     Enter the index number: 1

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Print list
     2. Add contact
     3. Modify contact
     4. Delete contact
     5. Exit the program

     Enter menu choice: 1

     ================== CONTACT LIST ==================
     Index   First Name            Last Name
     ======  ====================  ====================
     0       Richard               Stallman              
     1       Tim                   Cook                  

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Print list
     2. Add contact
     3. Modify contact
     4. Delete contact
     5. Exit the program

     Enter menu choice: 4

     Enter the index number: 5
     Invalid index number.

           *** TUFFY TITAN CONTACT MAIN MENU

     1. Print list
     2. Add contact
     3. Modify contact
     4. Delete contact
     5. Exit the program

     Enter menu choice: 5
     ```

1. Run the unit testing program to ensure that your program runs as expected.
    
    For Linux and Mac users
    ```
    ./test.sh
    ```
       
    For windows users
    ```
    ./win_test.bat
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./test.sh` or `./win_test.bat` repeatedly until it passes all the test.

## Submission

Submit a zip file containing all the code files on canvas 

Naming Convention: CWID_LastName.zip  

Your zipped folder should contain below files:
```
CWID_LASTNAME.zip -
                  | > test.py
                  | > test.sh
                  | > main.py
                  | > contacts.py
                  | > test.txt
                  | > win_test.bat
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|Environment setup and Lab Submission|
|15|main.py file submitted contains the main driver program and meets the program requirements|
|15|contacts.py file submitted contains the contacts module and meets the program requirements|
|4|unit test passes Test01_AddContact|
|4|unit test passes Test02_ModifyContact|
|4|unit test passes Test02_ModifyContact Invalid Index Number|
|4|unit test passes Test04_DeleteContact|
|4|unit test passes Test04_DeleteContact Invalid Index Number|
