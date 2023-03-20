import sys

# store in and read from csv

class Employee:
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

    def applyRaise(self, magnitude):
        self.pay = self.pay * float(magnitude)
        return int(self.pay)

    def getEmployeeProperties(self):
        personnel = input("Enter an employee id: ")
        try: 
            personnel = int(personnel)
        except ValueError:
            print("Not a valid id!")
            sys.exit(1)

        employeeIDList = [employee.id for employee in employees]
        for employee in employees:
            if employee.id == personnel:
                menuOptions = ["Select an action:",\
                        "==============",\
                        "1. Get First Name",\
                        "2. Get Last Name",\
                        "3. Get Full Name",\
                        "4. Get Pay",\
                        "5. Change ID",\
                        "6. Raise Pay"]

                result = ''
                for option in menuOptions:
                    result += f'{option}\n'
                result += ">>> "

                option = input(f'{result}')
                if option == '1':
                    return employee.firstName
                elif option == '2':
                    return employee.lastName
                elif option == '3':
                    return f'{employee.firstName} {employee.lastName}'
                elif option == '4':
                    return employee.pay
                elif option == '5':
                    oldId = employee.id
                    newId = int(input("Enter a new id: "))
                    if newId not in employeeIDList:
                        employee.id = newId
                        return f'Updated Employee Id {oldId} to {newId}'
                    else:
                        return f"id {newId} already exist"
                elif option == '6':
                    oldPay = employee.pay
                    magnitude = input('Enter a magnitude for pay adjustment: ')
                    employee.pay = employee.applyRaise(magnitude)
                    return f'Updated Employee pay from {oldPay} to {employee.pay}'
            
        return 'Employee does not exist!'



employees = []
emp1 = Employee(1, "Hohn", "Jammy", 500000)
emp2 = Employee(2, "Moike", "Wasowski", 10000)
employees.append(emp1)
employees.append(emp2)
print(emp1.getEmployeeProperties())
