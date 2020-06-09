'''3. В массиве случайных
целых чисел поменять местами
минимальный и максимальный элементы.
1. create random list
2. change last[len+1] and first[0]'''
import random

array = [random.randint(0,100) for _ in range(100)]

print(array)

def change_pos(a):
    b = a[0]
    c = a[-1]
    a[0] = c
    a[-1] = b
    return a

print(change_pos(array))
