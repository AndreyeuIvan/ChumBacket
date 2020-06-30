'''Sololearn practice'''
numbers = ['one', 'two', 'three', 'four']
num_dict = {x[0]: x for x in numbers } # {'o': 'one', 't': 'three', 'f': 'four'}
print(num_dict['t']) # four

#dalay of 1 minute
import time
#time.sleep(60)

#output
def fun(a,b,c,d,e,f):
    return a*b-c/d+e%f # 2-3/4 +5
print(fun(1,2,3,4,5,6))

arr = (1,2,3,4,3,2,1)
a = list(map(lambda x: x%2 == 0, arr))
print(len(a))
print(a)

# try/except
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
    
a = 5
b = 7
try:
    a = a % b
except ZeroDivisionError:
    a = 0
else:
    b = 2
finally:
    print(a*b)

#string
string = 'SOLOLEARN'.capitalize()
cond = False

for i, n in enumerate(string):
    if cond:
        print(n, end='')
    else:
        print(i, end='')
    cond = not cond

# lists
k = [[1,2,3,4,5,6]]
k.append(7)
k.insert(1,8)
print(len(k))

#compare
def compare(x,y):
    import pdb;pdb.set_trace()
    if(x<y):
        return x
    print(x)
compare(8,7)
