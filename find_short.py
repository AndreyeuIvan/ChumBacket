def find_short(s):
    s = s.split()
    h = {}
    for index, i in enumerate(s):
        h[index] = len(i)
    l = min([(value, key) for key, value in h.items()])[0]
    return l # l: shortest word length

print(find_short("turns out random test cases are easier than writing out basic ones"))
