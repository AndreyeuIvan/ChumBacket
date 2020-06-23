'''classmethod as constructor'''

class Employee:

    num_of_emps = 0
    raise_amt= 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        pass

    def __str__(self):
        pass
    
class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        self.prog_lang = prog_lang
        super().__init__(first,last,pay)
        

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employess = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', '!@#', 50000, 'Python')
dev_2 = Developer('John', '!@#', 50000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000 , [dev_1])

print(mgr_1.email)

mgr_1.print_emps()
mgr_1.add_emp(dev_2)
print('*' * 50)
mgr_1.print_emps()
print('*' * 50)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
print('*' * 50)
print(issubclass(Manager, Employee))
#print(dev_1.email)
#print(dev_1.prog_lang)
#dev_1.apply_raise()
#print(dev_1.pay)




