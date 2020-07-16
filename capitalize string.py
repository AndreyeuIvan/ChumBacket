import re


def to_camel_case(text):
    return ''.join(re.split(r'[-_]', text.title()))
    

print(to_camel_case('hello_world'))
print(to_camel_case('the-stealth-warrior'))
'def to_camel_case(text):
    return ''.join(x for x in text.title() if not x.isspace())
'
    
    
