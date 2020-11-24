class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """ Initialize name and age attribute."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dig sitting in response to a command."""
        return self.name.title() + ' is now siting.'

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        return self.name.title() + ' rolled over!'


my_dog = Dog('willie', 6)
your_dog = Dog('licy', 3)

print(my_dog.roll_over())

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog's name is " + str(my_dog.age) + ' years old.')
print(my_dog.sit())
print()
print("My dog's name is " + your_dog.name.title() + '.')
print("My dog's name is " + str(your_dog.age) + ' years old.')
print(your_dog.sit())

# 9.1
"""Here I will store my hometasks"""


class Restaurant:
    """A simple attemt to create a restaurant"""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def decribe_restaurant(self):
        return f'Welcome in our {self.name}. We are serving {self.cuisine_type} dishes'

    def open_restaurant(self):
        return f'{self.name} is open'

    def set_number_server(self):
        """Set up a number of served people"""
        return f' We served {self.number_served} people'

    def increment_number_server(self, increment_number):
        """Add the given amount to the number of servants"""
        self.number_served += increment_number


print()
res = Restaurant('Oliver', 'Meat')
res_1 = Restaurant('Stone', 'Soup')
res_2 = Restaurant('Kill', 'Bill')
print(res_1.decribe_restaurant())
print(res_2.decribe_restaurant())
print(res.decribe_restaurant())
print(res.open_restaurant())

# 1 method
print('1 method')
res_3 = Restaurant('Hello', 'World')
res_3.number_served = 5
print(res_3.number_served)
res_3.number_served = 10
print(res_3.set_number_server())
res_3.increment_number_server(300)
print("Let's now increment number of servants on 300")
print(res_3.set_number_server())


class User:
    """Here I will store a simple user"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        return f'This is a user {self.first_name} {self.last_name}'

    def greet_user(self):
        """Lets greet our user"""
        return f'Hello {self.first_name} {self.last_name}'

    def increment_login_attempts(self):
        """Add the login value into increment """
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('Ivan', "Andreyeu")
user_1 = User('Tvoi', 'Master')

print(user.describe_user())
print(user_1.describe_user())
print(user_1.greet_user())

user.increment_login_attempts()
user.increment_login_attempts()
print(f'We have incremented by {user.login_attempts} login attempts')
user.reset_login_attempts()
print('We decided that to reset login attempts and now they are', user.login_attempts)


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_desctiptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        return f'This car has {self.odometer_reading} miles on it'

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            return 'You can\'t roll back an odometer'

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_desctiptive_name())

my_new_car.update_odometer(-100)
print(my_new_car.read_odometer())

my_new_car.update_odometer(23500)
print(my_new_car.read_odometer())

my_new_car.increment_odometer(100)
print(my_new_car.read_odometer())


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """return a statement describing the battery size."""
        return f'This car has a {self.battery_size} -kWh battery/'

    def get_range(self):
        """Return a statement about the range this battery provides"""
        c_range = 0
        if self.battery_size == 70:
            c_range = 240
        elif self.battery_size == 85:
            c_range = 270
        return f'This car can go approximately {c_range} miles on fill charge'

    def upgrade_battery(self):
        """Should upgrade every battery, if it is < 85"""
        if self.battery_size == 70:
            self.battery_size == 85


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vihicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parents class.
        Then initiate attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        return 'This car does not need a gas tank'


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_desctiptive_name())
print(my_tesla.battery.describe_battery())
print(my_tesla.fill_gas_tank())
print(my_tesla.battery.get_range())
print('LEts update battery')
my_tesla.battery.upgrade_battery()
print(my_tesla.battery.battery_size)
print(my_tesla.battery.get_range())


class IceCreamStand(Restaurant):
    """Create a specific restaurant"""

    def __init__(self, name, cuisine_type, flavors):
        super(IceCreamStand, self).__init__(name, cuisine_type)
        """Initialize IceCreamStand"""
        self.flavors = flavors

    def return_flavors(self):
        """Here we will represend a list of flavors"""
        return f"Hello we have this flavors {', '.join(self.flavors)}"


ice = IceCreamStand('ICe', 'Ice-cream', ['vanila', 'banana', 'mango'])
print(ice.return_flavors())


class Privilages:

    def __init__(self, privilages=None):
        if privilages is None:
            privilages = ['can add post', 'can delete post', 'can ban user']
        self.privilages = privilages

    def show_privilages(self):
        """Method will return privilages provided by Admin"""
        return f"Hello we have a list of privilages:{', '.join(self.privilages)}"


class Admin(User):
    """Creating new class from User """

    def __init__(self, first_name, last_name):
        """Initialize method with new attribure privilages"""
        super().__init__(first_name, last_name)
        self.privilages = Privilages()


admin = Admin('My', 'NEW ADMIN')
print(admin.privilages.show_privilages())
