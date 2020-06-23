'''Working with generators. Firstly, create generated list, than generator, then compare'''
list_generated = [x for x in range(10)]
gen = (x for x in range(10))

print(list_generated,gen)

def genex(value):
    i = 0
    while i < value:
        yield i
        i += 1


for i in genex(10):
    print(i)
