list_1 = [1,2,3,4,5]
list_2 = [1,2,3,4,6]
list_3 = [1,2,3,4,7]
list_4 = [1,2,3,4,8]
list_5 = [1,2,3,4,9]

final_list = [list_1, list_2, list_3, list_4, list_5]

l = []

for i in final_list:
    l.append(i[-1])
print(l)
print([x.pop() for x in final_list])
