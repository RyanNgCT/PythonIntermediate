class Employee:
    # constructor
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f'{self.firstName}@{self.lastName}.io'

emp1 = Employee("Hohn", "Jammy", 500000) # instantiating employee objects
emp2 = Employee("Moike", "Wasowski", 10000)

# emp1.firstName = "Hohn"
# emp1.lastName = "Jammy"
# emp1.email = f'{emp1.firstName}@{emp1.lastName}.io'

print(f'Email 1: {emp1.email}\nEmail 2: {emp2.email}')