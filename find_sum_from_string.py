'''
x = 43
return 7'''

def sum_str(n: str):
    #import pdb;pdb.set_trace()
    result = [int(n[num]) for num in range(len(n))]
    #for num in range(len(n)):
        #result.append(int(n[num]))
    
    return sum(result)

print(sum_str('43'))

