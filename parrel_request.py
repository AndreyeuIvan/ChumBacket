'''Sending parrallel requests '''
import concurrent.futures as cc
import requests
import time

def single_request(url):
    r = requests.get(url)

sites = [
    'https://www.google.com',
    'https://www.google.com',
    ] * 5

start_time = time.time()

with cc.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(single_request, sites)

duration = time.time() - start_time
print(f'Total Time {len(sites)} in {duration} seconds')

