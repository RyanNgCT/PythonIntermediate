class Employee:
    raiseAmount = 1.05
    numOfEmps = 0
    numOfSubs = 0

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


class Manager(Employee):
    # Manager supervises the following employees (default of None)
    def __init__(self, id, firstName, lastName, pay, subordinateList= None):
        super().__init__(id, firstName, lastName, pay)
        if subordinateList is None:
            self.subordinates = []
        else:
            self.subordinates = subordinateList

    def addSubordinate(self, subordinate):
        if subordinate not in self.subordinates:
            self.subordinates.append(subordinate)
            Employee.numOfSubs += 1

    def removeSubordinate(self, id):
        if self.subordinates != []:
            for subordinate in self.subordinates:
                if subordinate.id == int(id):
                    self.subordinates.remove(subordinate)
                    Employee.numOfSubs -= 1
                    print(f'Employee {subordinate.firstName} successfully removed.')
                    return 'Get noOfSubs'
                else:
                    continue
            return f'Employee {id} doesn\'t exist / already removed from list.'
        else:
            return "Employee list is empty."


class Developer(Employee): # inherits all attributes from Employee class
    raiseAmount = 1.07
    def __init__(self, id, firstName, lastName, pay, progLang):
        super().__init__(id, firstName, lastName, pay) # use parent to initialize properties specified

        # alternative code
        # # Employee.__init__(self, id, firstName, lastName, pay)
        self.progLang = progLang


emp1 = Employee(1, "Hohn", "Jammy", 500)
emp2 = Developer(2, "Moike", "Wasowski", 150, "Java")
emp3 = Manager(3, "Jim", "Sully", 300)
print(f'{emp2.firstName}\'s pay is ${emp2.pay}.')
#print(f'{emp3.firstName}\'s pay is ${emp3.pay}.')

# check if emp2/devlpr is an instance of emp class
print(isinstance(emp2, Employee)) 

# check if developer subclass of emp class
print(issubclass(Developer, Employee))

emp2.applyRaise()

print(f'{emp2.firstName}\'s pay after the raise is ${int(emp2.pay)} and he learns {emp2.progLang}.')

while True:
    option = input('\nMenu:\n=======\n(1) Add an Employee\n(2) Remove an Employee\n(3) Exit\n>>> ')
    if option == "1":
        emp3.addSubordinate(emp1)
        emp3.addSubordinate(emp2)
        print(f'{emp3.firstName}\'s has {emp3.numOfSubs} subordinates after the addition.')
    elif option == "2":
        empId = input('Enter employee id to remove: ')
        res = emp3.removeSubordinate(empId)
        if res == 'Get noOfSubs':
            print(f'There are {Employee.numOfSubs} subordinates for Employee {emp3.firstName} left.')
        else:
            print(res)
    elif option == "3":
        break
    else:
        print('Invalid option!')

