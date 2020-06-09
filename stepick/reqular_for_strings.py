import re

with open('/home/ivar/Downloads/dataset_3363_2.txt', 'r') as f:
    s = f.read()
    
def string_counter(s:str):
    regex = r'(\w)(\d*)'
    
    list_a = re.findall(regex, s)
    
    l = []
    for i in list_a:
        l.append(list(i))
	
    string = ''
    for i in l:
        string += i[0] * int(i[1])
    return string

print(string_counter(s))
