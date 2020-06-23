def nextSquare(x):
    x **= 0.5
    x += 1
    x **= 2
    
    print(x, end = ", ")
    return x
    
print(nextSquare(25))

    
from math import sqrt
    
def inc(x):
    return x + 1 
    
def fnextSquare(x):

    print(x, end = ", ")
    
    return pow(inc(sqrt(x)), 2)
    
print(fnextSquare(25))


def func(lst, n):

    for i in range(n):

        lst.append(i)

    return lst


initial_list = [1, 2, 3]

resulting_list = func(initial_list, 3)

print(initial_list, resulting_list)
