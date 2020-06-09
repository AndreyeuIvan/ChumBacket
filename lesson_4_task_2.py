'''1 Task:
    1.Choose a simple earlier created HW algorithem.
    2.Create 2 variense of code
    3.Analyse and choose perfect one
    4.Create comments with a result of testing
    5. Create commone conclusion

    2. Task:
    1. Algorithem of Eratospen
    2. Write own, compare'''



def eratospen(n):
    
    sieve = [x for x in range(n)]
    sieve[1] = 0

    for i in range(2,n):
        if sieve[i] != 0:
            j = i * 2
            
            while j < n:
                sieve[j] = 0
                j += i

    return [i for i in sieve if i!=0 ]
    


def my(n):
    lst = []
    k = 0

    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            lst.append(i)
        else:
            k = 0
    return lst

#eratospen(20)
#1000 loops, best of 3: 5.63 usec per loop
#my(20)
#1000 loops, best of 3: 17.7 usec per loop

#eratospen(30)
#1000 loops, best of 3: 8.02 usec per loop
#my(30)
#1000 loops, best of 3: 33.7 usec per loop

#eratospen(300)
#1000 loops, best of 3: 84 usec per loop
#my(300)
#1000 loops, best of 3: 2.6 msec per loop


