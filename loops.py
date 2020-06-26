a, b, c, d = int(input('enter value a:')), int(input('enter value b:')), int(input('enter value c:')), int(input('enter value d:'))


for i in range(a,b):
   for j in range(c,d):
      k = i*j
      print (k, end=' ')
   print()
