'''Напишите программу, на вход которой подаётся прямоугольная матрица
в виде последовательности строк, заканчивающихся строкой,
содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера,
у которой каждый элемент в позиции i, j равен сумме
элементов первой матрицы на позициях (i-1, j),
(i+1, j), (i, j-1), (i, j+1). У крайних символов соседний
элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является
соседом по соответствующему направлению.'''

a = []
while True:
    s = input('Enter Value')
    if s == 'end':
        break
    input_value = [int(x) for x in s.split()]
    a.append(input_value)
print(a)
