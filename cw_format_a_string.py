"""Return: a string formatted as a list
of names separated by commas except for the last two names,
which should be separated by an ampersand.
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''"""
def list_transform(l:list):
    l_new = l[:]
    if len(l_new) == 1:
        l_new.insert(1,l_new.pop().get('name'))
    elif len(l_new) == 0:
        return ""
    else:
        for i in range(0, len(l_new)):
            if i == len(l_new)-1:
                l_new.insert(i,'& ' + l_new.pop(i).get('name'))
            else:
                l_new.insert(i,l_new.pop(i).get('name'))
            #print(i, l_new)
    new_string = ', '.join(l_new)
    new_string = new_string.replace(', &',' &')
    return str(new_string)
            
        

print(list_transform([]))
print(list_transform([{'name': 'Bart'}]))
print(list_transform([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(list_transform([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Lisa'}]))
