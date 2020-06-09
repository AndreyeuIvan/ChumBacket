import re

with open ('dataset_3363_2.txt', 'r') as f:
    s = f.read()
    
s = s.lower()
print(s)

for i in re.findall(r'(\D)(\d+)', s):
 print(i[0]*int(i[1]), end="")
