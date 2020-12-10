form xml2json import json2xml

with open ('currency.xml') as f:
    print(json2xml(f))