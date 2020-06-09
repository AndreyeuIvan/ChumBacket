'''first add path into file,
second step: enter path into requests,
thierd step:get new path,
forth step: correct string
fifth step: enter path into requests
if endswith('We'):
return text else: recursion'''
import requests
import os

os.chdir('/home/ivar/Downloads')

with open('dataset_3378_3(2).txt', 'r') as f:
    file = f.read().split()[0]


def steppick(file:str):
    if file.startswith('We'):
        return file
    else:
        r = requests.get(file)
        file = file[:-len(r.text)] + r.text
        print(file)
        steppick(file)
        
print(steppick(file))
