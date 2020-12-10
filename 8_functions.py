def greet_user(username):
    print('Hello,'+username.title() + '!')

greet_user('Ivar')

def display_message():
    return 'Function is perfect'

print(display_message())

def favorite_book(book):
    return f'One of my favorite books is {book}.'

print(favorite_book('Harry Potter'))

#pet.py
def describe_pet(animal, name):
    return f'\n I have a {animal}.\n My {animal}\'s name is {name.title()}'

print(describe_pet('dog', 'Doggi'))
print(describe_pet('cat', 'cotty'))


def list_sum(b,a = []):
    a.append(b)
    return a

print(list_sum('b'))
    
def make_shirt(size = 'L', text:str = 'I love python') -> str:
    return f'You have {size} size of t-shirt with {text.title()} as a slogan'

print(make_shirt())
print(make_shirt('M', 'Hallo World'))

def describe_city(city:str, country:str):
    return f'{city} is in {country}'

print(describe_city('Minsk', 'Belatus'))
