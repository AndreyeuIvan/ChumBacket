a = int(input('enter'))
b = int(input('enter'))
my_list=[]

for i in range(a,b+1):
    if i % 3 == 0:
        my_list.append(i)

print(sum(my_list)/len(my_list))
