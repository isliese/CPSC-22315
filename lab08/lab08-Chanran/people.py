# Name : Chanran Kim 
# Date : 11/05/2024

# A class named `Person`
class Person: 

    # __init__ member function
    def __init__(self, firstname="", lastname=""):
        self.firstname = firstname
        self.lastname = lastname

# A class named `Faculty` that inherits from `Person`
class Faculty(Person):

    # __init__ member function 
    def __init__(self, firstname="", lastname="", department=""):
        super().__init__(firstname, lastname)
        self.department = department

# A class named 'Student' that inherits from `Person`
class Student(Person):

    # __init__ member function
    def __init__(self, firstname="", lastname=""):
        super().__init__(firstname, lastname)
        self.classyear = ""
        self.major = ""
        self.advisor = None

    # set_class member function
    def set_class(self, classyear=""):
        self.classyear = classyear

    # set_major member function
    def set_major(self, major=""):
        self.major = major
    
    # set_advisor member function
    def set_advisor(self, advisor):
        if isinstance(advisor, Faculty):
            self.advisor = advisor
    
