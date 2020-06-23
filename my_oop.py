class Unicorn:

    new_a = 3
    
    def __init__(self, age, name, second_name, prev_job):
        self.age = age
        self.name = name
        self.second_name = second_name
        self.prev_job = prev_job

    def full_name(self):
        return self.name + self.second_name

    def new_age(self):
        self.age = int(self.age + self.new_a)
    
class Developer_py(Unicorn):

    def __init__(self, age, name, second_name, prev_job, skills):
        super().__init__(age, name, second_name, prev_job)
        self.skills = skills
        
class Django_dev(Unicorn):
    pass

un_1 = Unicorn(25, 'Ivan', 'Andreyeu', 'accountant')
un_2 = Unicorn(27, 'Sepgey', 'Gurkov', 'bartender')
un_3 = Unicorn(26, 'Alena', 'Volockova', 'drawer')
un_4 = Unicorn(44, 'Alena', 'Kushnarevich', 'analysist')

dev_1 = Developer_py(25, 'Ivan', 'Andreyeu', 'accountant', 'Sap')

print(un_1.full_name())
un_2.new_age()
print(un_2.age)
print(un_2.__dict__)

print(dev_1.new_age())
print(dev_1.age)
'''1. Work on classmethod, staticmethod
    2. magic methods
    3. What is decorators'''
