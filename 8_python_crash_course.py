def display_message():
    """Will show message"""
    return 'Argument and parameter is same thing. Function is very usefull thing'


print(display_message())


def favorite_book(title):
    """8.2 Favorite book"""
    return f'One of my favorite books is {title}'


print(favorite_book('Alice in Wonderland'))


def make_shirt(size, text):
    """T-shirt will be made by this function"""
    return f'T-shirt have {size} and {text} on it'


print(make_shirt(46, 'Hello World'))


def make_shirt(size='L', text='I Love Python'):
    """T-shirt function modifyed"""
    return f'T-shirt have {size} and {text} on it.'


print(make_shirt())
print(make_shirt('M', 'I love Parseltong'))


def city_county(city, county):
    """Function will displays city and county name"""
    return f'"{city}, {county}"'


print(city_county('Santiago', 'Chile'))
print(city_county('Minsk', 'Belarus'))
print(city_county('Moskow', 'Russia'))


def make_album(artist, album, track=''):
    """Creating function in order to create dict in return"""
    music = {'artist': artist, 'album': album}
    if track:
        music['track'] = track
    return music


print(make_album('Bill', 'The first'))
print(make_album('Python', 'Hello World'))
print(make_album('ABBA', 'First Album'))
print(make_album('ABBA', 'Second Album', track='16'))

while True:
    break
    print('Enter q to quit')
    artist = input('Enter artist')
    if artist == 'q':
        break
    print('Enter album')
    album = input('Enter album')
    if album == 'q':
        break
    print(make_album(artist, album))

mags = ['Albus', 'Severus', 'Snap']


def show_mag(mags):
    """Func will returne names of magicians"""
    for mag in mags:
        return mag


def make_great(mag):
    mag_new = mag[:]
    return f'the Gerat{mag_new}'


print(make_great(show_mag(mags)))


def sandwiches(*items):
    """Create Sandwitch-func, what returns items from list of items"""
    return items


print(sandwiches('ham', 'cucumber', 'olives'))


def build_profile(first, last, **user_info):
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


print(build_profile('Ivan', 'Andreyeu',
                    locatiom = 'Minsk',
                    field = 'Programming',
                    age = 18))


def make_car(manufacturer, model, **car_info):
    profile = {}
    profile['manuf'] = manufacturer
    profile['model'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile


print(make_car('subaru',
               'outback',
               color='blue',
               tow_package=True))
