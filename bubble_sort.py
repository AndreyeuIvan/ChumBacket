def bubble_sort(array):
    n = len(array)
    import pdb;pdb.set_trace()
    for i in range(n):
        already_sorted = True

        for j in range(n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False
        if already_sorted:
            break

    return array

print(bubble_sort([10,3,1,9,8,4,2,7]))
