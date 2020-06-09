'''1 Task:
    1.Choose a simple earlier created HW algorithem.
    2.Create 2 variense of code
    3.Analyse and choose perfect one
    4.Create comments with a result of testing
    5. Create commone conclusion

    2. Task:
    1. Algorithem of Eratospen
    2. Write own, compare'''

n = int(input('Enter value for checking:'))

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
    
print(eratospen(n))

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
print(my(n))

