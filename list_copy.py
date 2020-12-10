# Lets Try copy lists in 2 different ways

list_1 = [x for x in range(0,3)]

#Simple one, by using =
list_2 = list_1
print('before append', list_2, list_1)
list_1.append(2)

print('after append 2 into 1 list',list_2, list_1)
print('&'*50)
#By coping slices
list_2 = list_1[:]
print('before append [:]:', list_2, list_1)
list_2.append(3)

print('after append [:]',list_2, list_1)

