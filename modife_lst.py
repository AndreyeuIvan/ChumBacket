'''Напишите функцию modify_list(l),
которая принимает на вход список целых чисел,
удаляет из него все нечётные значения, а чётные нацело делит на два.
Функция не должна ничего возвращать,
требуется только изменение переданного списка, например:'''
def modife_list(l: list):
    #import pdb; pdb.set_trace()
    for i in l:
        if i % 2 == 0:
            l.remove(i)
        else:
            l.append(i//2)
            l.remove(i)

print(modife_list([1,2,3]))
lst = [1, 2, 3, 4, 5, 6]
print(modife_list(lst))

            
        
