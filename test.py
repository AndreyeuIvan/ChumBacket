def unique_names(names1, names2):
    my_list = []
    my_list.extend(names1)
    my_list.extend(names2)
    my_list.sort()
    return my_list

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
