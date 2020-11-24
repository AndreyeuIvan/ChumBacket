alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    print('+5 points')
else:
    print('Done')

#5.4
alien_color = 'green'
if 'green' in alien_color:
    print('+5 points')
elif 'green' not in alien_color:
    print('+10 points')

alien_color = 'black'

if 'green' in alien_color:
    print('+5 points')
else:
    print('+10 points')
    

#5.5
    #1 v
alien_color = 'red'
if 'green' is alien_color:
    print('+5 points')
elif 'yellow' is alien_color:
    print('+10 points')
elif 'red' is alien_color:
    print('+15 points')
else:
    print('+10 points')

    #2 v
alien_color = 'yellow'
if 'green' is alien_color:
    print('+5 points')
elif 'yellow' == alien_color:
    print('+10 points')
elif 'red' == alien_color:
    print('+15 points')
else:
    print('+10 points')


    #3 v
alien_color = 'green'
if 'green' == alien_color:
    print('+5 points')
elif 'yellow' == alien_color:
    print('+10 points')
elif 'red' == alien_color:
    print('+15 points')
else:
    print('+10 points')


#5.6
person = 2
if person < 2:
    print('This is a Baby')
elif person < 4:
    print('This is a toddler')
elif person < 13:
    print('This is a kid')
elif person <20:
    print('This is a teenager')
elif person < 60:
    print('This is an adult')
else:
    print('This is an elderly')

#5.7
fruits = ['apple', 'banana', 'pineapple']

if 'apple' in fruits:
    print('You like apples')
elif 'banana' not in fruits:
    print('Banana')
elif 'banana' not in fruits:
    print('Banana')
elif 'pineapple' in fruits:
    print('You are lover of bababas')
else:
    print('Bye')

#5.8
users = ['admin', 'user', 'player', 'log', 'me']

if users:
    [print(f'Hello Eric, thanks for logging') for user in users if user == 'admin' ]
else:
    print('We need to find some users')

#5.10
current_users = ['me','you', 'guest', 'admin', 'cheese']
new_users = ['he','me', 'you', 'dancer', 'singer']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('Enter new username')
    else:
        print('USername is avalable')
#5.11
ordinal = [1,2,3]

[print(x) for x in range(0,10)]

store = [x for x in range(0,10)]
print(store)
for x in store:
    if x == ordinal[0]:
        print(str(x) + 'st')
    elif x == ordinal[1]:
        print(str(x) + 'nd')
    elif x == ordinal[2]:
        print(str(x) + 'rd')
    else:
        print(str(x) + 'th')

