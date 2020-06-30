'''Practice try/except blog'''
def calc(n):
    try:
        n = int(n)
    except Exception:
        print('_error_')
        n = 0
    else:
        return 10 * n/1000

print(calc(1000))
