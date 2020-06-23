'''Working with decorators
propery allows take of () from method'''

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + '.' + last + '@company.com'
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('DElete')
        self.first = None
        self.last = None
    
emp_1 = Employee('John', 'Smith', 100)

emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
