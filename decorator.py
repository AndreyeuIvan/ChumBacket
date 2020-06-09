'''Creating decorator'''
def header(func):

    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner

def table(func):

    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner

@header
@table
def say(name,surname,age):
    print('Hello World',name,surname,age)


say('V','S',30)

