a, b, c, d = int(input('Enter:')),int(input('Enter:')),int(input('Enter:')),int(input('Enter:'))
max1 = max(a,b,c,d)
min1 = min(a,b,c,d)
for j1 in range(c, d+1):
    print(j1, end= '')
for i in range(min1, max1+1):
    for j in range(c,d+1):
        print(i,i*j, end= '\t')
    print()

#for i in range(a, b+1): #4
#    for j in range(c,d+1): #3
#      print(i, i*j, end='\t')
#print()

#n = int(input('f'))

#for i in range(1,n): #length
#   for j in range(2,n): # width
#       print('*', end= '\t')
#   print()
