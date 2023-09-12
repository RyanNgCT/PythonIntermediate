class Employee:

    # constructor
    def __init__(self, id, firstName, lastName, pay):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        #self.email = f'{self.firstName}_{self.lastName}@code.io'

    # original method
    @property
    def fullName(self): # only to pass in self as instance argument
        return f'{self.firstName} {self.lastName}'
    

    # setter method
    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ') # split input
        self.firstName, self.lastName = first, last
    
    # deleter method
    @fullName.deleter
    def fullName(self):
        # deletes the name of a given object
        self.firstName, self.lastName = None, None


    @property
    def email(self):
        if self.firstName != None and self.lastName != None:
            return f'{self.firstName}_{self.lastName}@code.io'
        return 'Invalid Email!'


emp_1 = Employee(1, "Hohn", "Jammy", 500)

emp_1.fullName = 'Moike Wasaowki' # Modify fullname and email tgt

# use dict comprehension and __dict__ method to extract attributes of Employee Object
print({key: value for key, value in emp_1.__dict__.items()})
print('email: ', emp_1.email) # no need to call implicitly

del emp_1.fullName

print({key: value for key, value in emp_1.__dict__.items()}, emp_1.email)