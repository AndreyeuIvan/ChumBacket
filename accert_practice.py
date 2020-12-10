import sys


def linux_interaction():
    assert('linux' in sys.platform), 'linux'
    print('Done')

try:
    linux_interaction()
except:
    pass
try: 
    1 / 0
except ZeroDivisionError: 
    print('Divided by zero')

print('Should reach here')
