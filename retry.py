'''Практика декораторов, используем ретри из статьи на медиуме'''

def my(x):
    return str(x)

my.yolo = 'you live only once'
print(my.yolo)

@con_2_num
def first(x):
    return x**2

def secont(x):
    return x - 2

def con_2_num(func):
    def new_f(x):
        return func(float(x))

    return new_f

new_1_func = con_2_num(first)
print(new_1_func('2'))
print(con_2_num(secont(2)))
