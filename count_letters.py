'''alphabet_position(The sunset sets at twelve o' clock.)
20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11 '''
from string import ascii_letters

def alphabet_position(text):
    '''Firstly create dict with letters as keys'''
    letters = ascii_letters[:26]
    hash_letters = {}
    for i, l in enumerate(letters, start = 1):
            hash_letters[l] = i
    '''Secondly return letters as numbers'''
    text = text.lower()
    my_list = []
    st = ''
    for i in text:
        if hash_letters.get(i) != None:
            my_list.append(hash_letters.get(i))
            st = ' '.join(str(e) for e in my_list)
    return st
print(alphabet_position('The sunset sets at twelve o clock'))
