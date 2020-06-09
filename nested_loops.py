import pdb
a = [
    [0,2,4,6],
    [1,5,4,5,6,8,9,13],
    [3,10,17,19]
]

'''for i in a:
    for j in i:
        j += 10
        #pdb.set_trace()
        print(j, end=' ')
    print()

print(a)'''

for j in range(4):
    for i in range(3):
        print(a[i][j], end= ' ')
    print()


