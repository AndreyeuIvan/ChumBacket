a = 7
b = 10
c = 5
d = 6


s = '\t'

for j in range(c, d+1):
    print(s,j, end = "")
    
print()    
for i in range(a, b+1):
    print(a, end = s)
    for n in range(c, d+1):
        k=a*n
        print(k, end = s)
    print()
    a+=1
    
