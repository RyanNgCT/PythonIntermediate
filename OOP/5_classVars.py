from multipledispatch import dispatch

class Employee:
    # class variables (access using className.variableName) -> differ from video
    raiseAmount = 200
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
    
    @dispatch(int)
    def applyRaise(self, magnitude):
        self.pay *= magnitude

    @dispatch()
    def applyRaise(self):
        self.pay += Employee.raiseAmount


emp1 = Employee(1, "Hohn", "Jammy", 500)
emp2 = Employee(2, "Moike", "Wasowski", 100)
print(f'{emp1.firstName}\'s initial pay is ${emp1.pay}, while {emp2.firstName}\'s initial pay is ${emp2.pay}.')

emp1.applyRaise()
emp2.applyRaise(10)
print(f'{emp1.firstName}\'s pay is updated to ${emp1.pay}, while {emp2.firstName}\'s pay is updated to ${emp2.pay}.')

print(f'\nEmployee 1 properties: {emp1.__dict__}')
print(Employee.numOfEmps)