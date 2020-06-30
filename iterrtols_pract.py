from itertools import *

for i in combinations('abc', 2):
    print(i, end = ' ')
print()
for i in permutations('abb'):
    print(i, end = ' ')
