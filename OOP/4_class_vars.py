import sys, os, csv

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
        return int(self.pay) # cast back

    def getEmployeeProperties(self, employees, e):
        employeeIDList = [employee.id for employee in employees]
        menuOptions = ["\nSelect an action:",\
                "==============",\
                "1. Get First Name",\
                "2. Get Last Name",\
                "3. Get Full Name",\
                "4. Get Pay",\
                "5. Change ID",\
                "6. Change Pay",\
                "7. Save current employee list as .csv file",\
                "8. Read new employees from .csv file", \
                "9. Quit the Program",\
                "10. Display all employee details"]

        result = ''
        for option in menuOptions:
            result += f'{option}\n'
        result += ">>> "

        option = input(f'{result}')
        if option == '1':
            return e.firstName
        
        elif option == '2':
            return e.lastName
        
        elif option == '3':
            return e.printFullName()
        
        elif option == '4':
            return e.pay
        
        elif option == '5':
            oldId = e.id
            newId = int(input("Enter a new id: "))
            if newId not in employeeIDList:
                e.id = newId
                return f'Updated Employee Id {oldId} to {newId}'
            else:
                return f"id {newId} already exist"
            
        elif option == '6':
            oldPay = e.pay
            magnitude = input('Enter a magnitude for pay adjustment: ')
            e.pay = e.applyRaise(magnitude)
            return f'Updated Employee pay from {oldPay} to {e.pay}'
        
        elif option == '7':
            pass

        elif option == '8': # CHORE: need to check for id clashes
            emp_count = 0
            filePath = input('Please specify the parent directory path to read from: ')
            filePath = os.path.abspath(filePath)
            with open(filePath) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for line in csv_reader:
                    line = list(line)
                    emp = Employee(int(line[0]), line[1], line[2], int(line[3]))
                    employees.append(emp)
                    emp_count += 1
                print(f'\n[INFO] {emp_count} employees loaded into program...\n')
            # can't use zero for return val as dealing with cost also
            return 'csv updated'

        elif option == '9':
            print('Quitting Program...')
            return
        
        elif option == "10":
            pass
            
        return 'Invalid option entered.'


employees = []
emp1 = Employee(1, "Hohn", "Jammy", 500)
emp2 = Employee(2, "Moike", "Wasowski", 100)
employees.append(emp1)
employees.append(emp2)

while True:
    personnel = input("Enter an employee id: ")
    try: 
        personnel = int(personnel)
    except ValueError:
        print("Not a valid id!")

    found = False
    for e in employees:
        if e.id == personnel:
            res = e.getEmployeeProperties(employees, e)
            if res != None and res != 'csv updated':
                found = True
                print(res)
            elif res == 'csv updated': 
                found = True # to satisfy flag (may need refactoring)
                continue
            else:
                sys.exit(1)

    if not found:
        print(f"Employee {personnel} not in current Employee List.")