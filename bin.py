import requests


url = 'https://httpbin.org/ip'
proxies = {
    'http' : 'http://209.50.52.162:9050',
    'https' : 'http://209.50.52.162:9050'
    }
r = requests.get(url, proxies=proxies)
print(responce.json())
