b = [int(i) for i in input('enter:').split()]
#import pdb; pdb.set_trace()
b.sort()
c = set()

for i in b:
    if b.count(i) >= 2:
        c.add(i)
        
print(' '.join(map(str, c)))
