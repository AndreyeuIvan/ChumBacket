''' Comprehension'''

data_set= [1,2,3,-9,-0,-11,4,-5,6]
new = None

collection = list()
for datum in data_set:
    if datum > 0:
        collection.append(datum)
    else:
        new = str(datum) + ' is negative digit' 
        collection.append(new)

print(collection)
print('Please compare to collections')
    
collection_2 = [d if d >0 else str(d)+' is negative digit' for d in data_set]
print(collection_2)
