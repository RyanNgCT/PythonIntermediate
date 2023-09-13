class Employee:
    raiseAmount = 1.05

    # constructor
    def __init__(self, id, firstName, lastName, pay):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f'{self.firstName}_{self.lastName}@code.io'

    # methods
    def printFullName(self): # only to pass in self as instance argument
        return f'{self.firstName} {self.lastName}'
    
    def applyRaise(self):
        self.pay *= Employee.raiseAmount

    # unambiguous representation of object -> meant for other devs to see
    def __repr__(self):
        return f"Employee('{self.firstName}', '{self.lastName}', {self.pay})"

    # to-string method
    def __str__(self):
        return f'{self.printFullName()} - {self.email}'
    
    # adds 2 employee's salaries together, other is next object to reference
    def __add__(self, other):
        return self.pay + other.pay


emp1 = Employee(1, "Hohn", "Jammy", 500)
emp2 = Employee(2, "Moike", "Wasowski", 150)

print(repr(emp1), repr(emp2))
print(str(emp1))

print(int.__add__(5, 3)) # using in-built function for type of int
print(emp1 + emp2)