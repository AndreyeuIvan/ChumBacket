def nb_dig(n, d):
    my_list = [str(x**2) for x in range(0,n+1) if str(d) in str(x**2)]
    s = 0
    for i in my_list:
        s += i.count(str(d))
    return s

print(nb_dig(5750,0))
print(nb_dig(11011,2))
print(nb_dig(12224,8))
print(nb_dig(11549,1))
