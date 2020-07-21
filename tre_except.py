try:
    f = open('test.txt')
except FileNotFoundError:
    print('Sorry, error')
except Exception:
    print('Fuck')
    
