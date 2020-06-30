'''Practice recursion'''

def s(my_list: list):
    s = 0

    #adding number into list
    for i in range(0, len(my_list)):
        s = s + my_list[i]

    return s

print(s([5,4,4,5]))

# recursively
def sum_1(my_list: list):
    if len(my_list) == 1:
        return my_list[0]
    else:
        return my_list[0] + sum_1(my_list[1:])

print(sum_1([5,4,4,5]))
