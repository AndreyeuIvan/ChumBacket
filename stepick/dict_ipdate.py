'''Напишите функцию update_dictionary(d, key, value),
которая принимает на вход словарь d d d и два числа:
key key key и value value value.

Если ключ key есть в словаре d,
то добавьте значение value в список,
который хранится по этому ключу.
Если ключа key нет в словаре,
то нужно добавить значение в список по ключу 2∗key.
Если и ключа 2∗key  нет,
то нужно добавить ключ 2∗key в словарь
и сопоставить ему список из переданного элемента [value].

Требуется реализовать только эту функцию, кода вне неё не должно быть.
Функция не должна вызывать внутри себя функции input и print.
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}'''

def update_dictionary(d, key, value):
    if key in d.keys():
        d[key].append(value)
    elif key in d.keys():
        d[2*key].append(value)
    elif 2*key not in d.keys():
        d.update({2*key:[value]})
        d[2*key] = []
d={} 
update_dictionary(d,1,-1)
update_dictionary(d, 2, -2)
update_dictionary(d, 1, -3)
