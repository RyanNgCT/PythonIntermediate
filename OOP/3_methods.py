class Employee:
    # constructor
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f'{self.firstName}@{self.lastName}.io'

    # methods
    def printFullName(self): # only to pass in self as instance argument
        return f'{self.firstName} {self.lastName}'

emp1 = Employee("Hohn", "Jammy", 500000) # instantiating employee objects
emp2 = Employee("Moike", "Wasowski", 10000)

# require parenthesis of method to get the return value => which is passed to print()
print(f'Employee 1\'s first name is: {emp1.printFullName()}')

# alternative
# test = Employee.printFullName(emp1)
# print(test)


