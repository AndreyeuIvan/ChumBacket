subject_marks = [('English', 88), ('Science', 90),
                 ('Maths', 97), ('Social sciences', 82)]

print('Original list of tuples:', subject_marks)

subject_marks.sort(key=lambda x: x[1])

print('\nSorting list of tuples:', subject_marks)


