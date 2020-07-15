def insert_sort(array):
    import pdb; pdb.set_trace()
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j>=0 and array[j] > key_item:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key_item
    return array

print(insert_sort([10,2,4,3,1,5,6]))
