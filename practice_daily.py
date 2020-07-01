'''daily practice'''
value = 0
def f(arg=1):
    arg = arg + 1
    return arg
print(f()+f(value))

class My:

    i = 0
    def __init__(self):
        i = 1
obj = My()
print(obj.i)

class Slack:
    def __init__(self):
        self.exists = True

    def __getattr__(self, name):
        print('__getattr__({})'.format(name))
        value = 'Value is {}'.format(name)
        setattr(self, name, value)
        return value

data = Slack()
print(data.foo)
data.foo = 13
print(data.foo)
