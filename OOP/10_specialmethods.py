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

    def __repr__(self):
        pass

    def __str__(self):
        pass

emp1 = Employee(1, "Hohn", "Jammy", 500)
emp2 = Employee(2, "Moike", "Wasowski", 150)