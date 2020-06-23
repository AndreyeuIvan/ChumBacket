import requests

#Firstly creating responce, we can check status by using ok or status_code, will provide us code of responce, by using headers we will get servers responce in dict 
r = requests.get('https://imgs.xkcd.com/comics/python.png')

r.ok
r.status_code
r.headers

r = requests.get('https://httpbin.org/get')
payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', prams=payload)
r.text

r = requests.post('https://httpbin.org/post', data=payload
payload = {'username': 'corey', 'password': 'testing'}
r.json()

r = requests.get('https://httpbin.org/get', auth=('user', '123'))
r. text
