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

emp_1 = Employee(1, "Hohn", "Jammy", 500)

emp_1.firstName = 'Jim' # email is still Hohn

# use dict comprehension and __dict__ method to extract attributes of Employee Object
print({key: value for key, value in emp_1.__dict__.items()})