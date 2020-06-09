import cProfile

def test_fib(func):
    lst = [0,1,1,2,3,5,8,13,21,34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

def fib(n):
    if n<2:
        return n
    return fib(n-1) + fib(n-2)

test_fib(fib)
        
# fib_test.fib(10)       
# 1000 loops, best of 3: 22.6 usec per loop

#fib_test.fib(20)
#1000 loops, best of 3: 2.79 msec per loop

#python3 -m timeit -n 1000 -s 'import fib_test' 'fib_test.fib(20)'

#cProfile.run('fib(15)')
#1976 function calls (4 primitive calls) in 0.001 seconds
#1973/1    0.001    0.000    0.001    0.001 fib_test.py:9(fib)

cProfile.run('fib(20)')
#21894 function calls (4 primitive calls) in 0.011 seconds
#21891/1    0.010    0.000    0.010    0.010 fib_test.py:9(fib)
