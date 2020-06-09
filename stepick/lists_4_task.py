a = [int(x) for x in input('Enter values:').split()]
sum_a = []
left_index = -1
right_index = -len(a)+1


if len(a) == 1:
    print(' '.join(map(str,a)))
else:
    for i in range(0,len(a)):
            sum_a.append(a[i+left_index]+a[i+right_index])
    print(" ".join(map(str,sum_a)))
