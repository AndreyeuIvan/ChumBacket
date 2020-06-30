'''Practice collection module'''
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = 'adadsfdsgdsf'
my_counter = Counter(a)
print(my_counter)
print(list(my_counter.elements()))

#Nametuple
Point = namedtuple('Point','x,y')
pt = Point(1, -4)
print(pt.x, pt.y)

#OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

#DefaultDict
d = defaultdict(list)
d['a'] = 1
d['b'] = 2
print(d['c'])

#Deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.pop()
print(d)
d.popleft()
print(d)
#d.clear()
#print(d)
d.extendleft([4,5,6])
print(d)
d.rotate(1)
print(d)
