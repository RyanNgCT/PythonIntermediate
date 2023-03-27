from multipledispatch import dispatch
import datetime

class Employee:
    raiseAmount = 1.05
    numOfEmps = 0

    # constructor
    def __init__(self, id, firstName, lastName, pay):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f'{self.firstName}_{self.lastName}@code.io'

        Employee.numOfEmps += 1 # need to use the Employee Class value per instance vs "self"

    # methods
    def printFullName(self): # only to pass in self as instance argument
        return f'{self.firstName} {self.lastName}'
    
    def applyRaise(self):
        self.pay *= Employee.raiseAmount

class Manager(Employee): # inherit from Employee class
    pass

class Developer(Employee): # inherits all attributes from Employee class
    raiseAmount = 1.07


emp1 = Employee(1, "Hohn", "Jammy", 500)
emp2 = Developer(2, "Moike", "Wasowski", 150)
emp3 = Manager(3, "Jim", "Sully", 300)

print(f'{emp2.firstName}\'s pay is ${emp2.pay}.')
print(f'{emp3.firstName}\'s pay is ${emp3.pay}.')

emp2.applyRaise()

print(f'{emp2.firstName}\'s pay after the raise is ${int(emp2.pay)}.')
