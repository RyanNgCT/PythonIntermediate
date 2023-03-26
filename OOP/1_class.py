class Employee:
    pass #skip for now

emp1 = Employee() # instantiating employee objects
emp2 = Employee()

# prone to mistakes when manually instantiating properties
emp1.firstName = "Hohn"
emp1.lastName = "Jammy"
emp1.email = f'{emp1.firstName}@{emp1.lastName}.io'

print(f'Email: {emp1.email}')