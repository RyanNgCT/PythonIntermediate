from multipledispatch import dispatch

class Employee:
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

    # defining class methods: add 'classmethod' decorator to top of method signature
    @classmethod
    def setRaiseAmt(cls, amount):
        cls.raiseAmount = amount


emp1 = Employee(1, "Hohn", "Jammy", 500)
emp2 = Employee(2, "Moike", "Wasowski", 100)

Employee.setRaiseAmt(500) # same as Employee.raiseAmount = 500

# All the same since we are working with classes rather than instances
# print(Employee.raiseAmount) 
# print(emp1.raiseAmount, emp2.raiseAmount)

rawEmp3 = '3-John-Doe-600'
rawEmp4 = '4-Ebenezer-Scrooge-1000'
rawEmp5 = '5-Callsign-Echo-200'

id, first, last, pay = rawEmp4.split('-') # split into string (used as props) -> sort of deconstruct
emp4 = Employee(id, first, last, pay) # init emp4
print(f'{emp4.firstName} {emp4.lastName} has an id of {emp4.id} and a pay of ${emp4.pay}.')
