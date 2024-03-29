# EmployeeApp v1, (c) RyanNgCT 2023

import sys, os, csv
from pathlib import Path

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
        self.pay = self.pay * magnitude
        return int(self.pay) # cast back
    
    def changePay(self, value):
        self.pay = value
        return value

    def getEmployeeProperties(self, employees, e):
        employeeIDList = [employee.id for employee in employees]
        menuOptions = ["Select an action:",\
                "==============",\
                "0. Quit the Program",\
                "1. Get First Name",\
                "2. Get Last Name",\
                "3. Get Full Name",\
                "4. Get Pay",\
                "5. Change ID",\
                "6. Change Pay",\
                "7. Save current employee list as .csv file",\
                "8. Read new employees from .csv file", \
                "9. Display all employee details", \
                "10. Delete an employee"]

        result = ''
        for option in menuOptions:
            result += f'{option}\n'
        result += ">>> "

        option = input(f'{result}')
        print()
        if option == '1':
            return e.firstName
        
        elif option == '2':
            return e.lastName
        
        elif option == '3':
            return e.printFullName()
        
        elif option == '4':
            return f'{e.firstName}\'s pay: ${e.pay}'
        
        elif option == '5':
            oldId = e.id
            try:
                newId = int(input("Enter a new id: "))
            except ValueError:
                return f'[ERROR] Not a valid id!'
                
            if newId not in employeeIDList:
                e.id = newId
                return f'[INFO] Updated Employee Id {oldId} to {newId}.'
            else:
                return f'[ERROR] Employee id {newId} already exist!'
            
        elif option == '6':
            internalOpt = input('Select an option:\n1) Change pay using magnitude\n2) Update pay manually\n>>> ')
            try: 
                internalOpt = int(internalOpt)
            except ValueError:
                return f'[ERROR] Not a valid numerical option entered!'
            if internalOpt == 1:
                oldPay = e.pay
                magnitude = input('Enter a magnitude for pay adjustment: ')
                try:
                    if float(magnitude) >= 0:
                        magnitude = float(magnitude)
                    else:
                        return f'[ERROR] Negative magnitude is not allowed!'
                except ValueError:
                    return f'[ERROR] Not a valid magnitude!'
                e.pay = e.applyRaise(magnitude)
            elif internalOpt == 2:
                oldPay = e.pay
                newPay = input('Enter a pay value in $: ')
                try: 
                    newPay = int(newPay)
                except ValueError:
                    return f'[ERROR] Not a valid pay value.'
                e.pay = e.changePay(newPay)
            else:
                return f'[ERROR] Enter an valid option (1/2) only!'
            return f'[INFO] Updated Employee pay from {oldPay} to {e.pay}'
        
        elif option == '7':
            employees.sort(key=lambda x:x.id)
            filePath = input('Please specify name of the output csv: ')
            currDir = os.getcwd()
            fullPath = currDir + os.sep + filePath
            emp_count = 0
            with open(fullPath, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                if employees != []:
                    for employee in employees:
                        lineFormat = [employee.id, employee.firstName, employee.lastName, employee.pay]
                        csv_writer.writerow(lineFormat)
                        emp_count += 1
                else: # by right shouldn't even allow no ids
                    return f'[ERROR] Employee List is empty. Populate Employee List first!'
            if emp_count == 1:
                return f'[INFO] Wrote 1 entry into {filePath}'
            else:
                return f'[INFO] Wrote {emp_count} entries into {filePath}'

        elif option == '8':
            emp_count = 0
            filePath = input('Please specify the file path to read from: ')
            filePath = str(Path(filePath).absolute()) # convert to absolute
            validPathCheck = Path(filePath).is_file()
            if validPathCheck:
                # open file for reading
                with open(filePath) as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for line in csv_reader:
                        line = list(line)
                         # block update for duplicate id
                        if int(line[0]) in employeeIDList:
                            return "[ERROR] Error in csv update, please check if employee already exist!"
                        # no duplicate, so update
                        else:
                            emp = Employee(int(line[0]), line[1], line[2], int(line[3]))
                            employees.append(emp)
                            emp_count += 1
                    print(f'\n[INFO] {emp_count} employees loaded into program...')
                    # can't use zero for return val as dealing with cost also
                    return '[INFO] Csv file updated.'
            else:
                return '[ERROR] File not found!'
        
        elif option == "9":
            # employeesSorted = [em.firstName for em in employees]
            employees.sort(key=lambda x:x.id)
            empInfoList = ""
            for employee in employees:
                empInfoList += f"[INFO] ({employee.id}) Employee {employee.printFullName()} has a salary of ${employee.pay} and email address of {employee.email}.\n"
            empInfoList += "===========Last Entry=========\n"
            return empInfoList
        
        elif option == "10":
            idToRemove = input("Enter Employee id to remove: ")
            try:
                idToRemove = int(idToRemove)
            except ValueError:
                return f'[ERROR] Please re-verify validity of id added!'
            if idToRemove not in employeeIDList:
                return f'[ERROR] employee to remove not found!'
            for employee in employees:
                if employee.id == idToRemove:
                    employees.remove(employee)
            #employees = list(filter(lambda x: x.id != idToRemove, employees))
            return f'[INFO] Done removing employee.'

        elif option == '0':
            print('[INFO] Quitting Program...')
            return
        else:
            return '[ERROR] Invalid option entered.'

employees = []
emp1 = Employee(1, "Hohn", "Jammy", 500)
emp2 = Employee(2, "Moike", "Wasowski", 100)
employees.append(emp1)
employees.append(emp2)

while True:
    flag = False
    personnel = input("\nEnter an employee id: ")
    print()
    if personnel != "":
        try: 
            personnel = int(personnel)
        except ValueError:
            flag = True
            print("[ERROR] Not a valid id!")
    else:
        flag = True
        print("[ERROR] Empty id. Try again...")

    found = False
    for e in employees:
        if e.id == personnel:
            res = e.getEmployeeProperties(employees, e)
            if res == None:
                sys.exit(1)
            # need to check if still needed
            # elif res == 'csv updated': 
            #     found = True
            #     continue
            elif res == '[ERROR] Error in csv update, please check if employee exist!': # duplicate entry
                found = True
                print("\nDuplicate id entry, please try again")
                continue
            else:
                found = True
                print(res)
                continue

    if flag:
        continue
    elif not found:
        print(f"[ERROR] Employee {personnel} not in current Employee List.")