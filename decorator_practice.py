'''from datetime import datetime

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

@timeit
def one(n):
    #start = datetime.now()
    l = []
    for i in range(n):
        if i % 6 == 0:
            l.append(i*2)
    #print(datetime.now() - start)
    return l

@timeit
def two(n):
    #start = datetime.now()
    l = [x*2 for x in range(n) if x % 6 == 0]
    #print(datetime.now() - start)
    return l

l1 = one(100)
l2 = two(100)

print(l1, l2)
'''




def dec(func):
    def wrap():
        print('before')
        func()
        print('after')
    return wrap

@dec
def print_test():
    print('test')

d = print_test()
print(d)
    
