from multipledispatch import dispatch
import datetime

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

    @classmethod
    def from_string(cls, empStr): #'alternative' constructor
        id, first, last, pay = empStr.split('-')
        return cls(id, first, last, pay) # return the constructor

    @staticmethod
    def isWorkDay(day):
        # Mon - 0, Sun - 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee(1, "Hohn", "Jammy", 500)
emp2 = Employee(2, "Moike", "Wasowski", 100)

#myDate = datetime.date.today()
myDate = datetime.date(2024,9,28)

isWorkDay = Employee.isWorkDay(myDate)
res = ''
if isWorkDay:
    res += f'{myDate} is a work/week day'
elif not(isWorkDay) and str(myDate) == '2024-09-28':
    res += f'WGT WADIO! Freedom at last.'
else:
    res += f'{myDate} is not a work day/is a weekend!'

print(res)