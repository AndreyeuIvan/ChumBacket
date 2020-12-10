import subprocess
from subprocess import PIPE


url_base = 'https://www.instagram.com/graphql/query/?'

command = f"""curl '{url}' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Referer: https://www.instagram.com/andgora/' -H 'Cookie: ig_did=A2F0D766-10AD-4A7B-8BB4-61CAACF18622; csrftoken=GX3C3ma5oEOQDXtvqR8mfUMHBnqtZjnR; mid=X84bWgAEAAHMpXC9LcBY-Uj2QW-O; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=360050299; sessionid=360050299%3Azesg6QQXJ7RDHg%3A18; shbid=3569; shbts=1607342978.500496; fbsr_124024574287414=4WLvTEY9T1U1xs_iR4BNLy17HsJRWSYyplP6FXME9Ws.eyJ1c2VyX2lkIjoiMTAwMDA1OTQzOTYyMTg0IiwiY29kZSI6IkFRQ3dGUy1zUlY4NTBLMUU5ME11Vy15WXo0Smp6eDhFSEpkNDdseHJTcVBNSVkxRzJCdlBxWUlocHRCc0pna3RrYzkzSDBudDVkblFYR0hWU2t3ajJ4ZWkwV3pTTUFDNmtGZjNIaWgxM2VvT3l1bXhPZklfNHZlVUlvdGRtTHJXMHdSZG40ZjBSV1hMaFJITV96eDl1ZlNjUjR6azB0ay1uMGJKY1FtQm5ScjBmWnR1NUYwTkh0S1RTMVFkeXM0Y0hZVV9hUjdsZkxIdlRubVFBREhORHZUeldkdGl0NFRyd1dSeVJfLW5wTjFjajV6QXVIUXFyT0xyYUpacUprZ2hVTGhLbGhrWURQdFhRaUUyalV1aDZoQXYxaEhuVHRmYXdleVZqSHItSmR6R2o5UFF4OGotUzBBVTFKMWdFT3dqRFk5WTY1ZXpnbWZtVEE2bElNbVFTa0hiIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUZGQTd4VEJqclNXNzQ3UUFvVnpTeTN3ZkNueGNLWHhnWFYzamtUbkxBTE1IUWFwa1pCTGtWRFdnck82N1FXTTNWWkJscWZQWkNRZ1ZzMWFna01oNldURjNKNGRLUUpPY2Rhb0FwOWNaQ25CWGJhUGVpaVNIOXFSeWVQQkRiNVBQSUp5YnVxaGk0d2tHclJaQWQ1QWdXTFlxU3lKMlZ4OUdsRHVpSmZ0bCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjA3MzQ3MjU0fQ; urlgen="{{\"178.127.94.144\": 6697}}:1kmGS0:sr59FozPeIcFcJfxRsYbHUSLD3E"; rur=FTW' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'TE: Trailers' > followers_{index}.json"""

result = subprocess.run(command, shell=True, stdout=PIPE, stderr=PIPE)

index = 1
while True:
   
    get_param = {
        'query_hash' : 'c699b185975935ae2a457f24075de8c7',
        'variables' : '%7B%22has_threaded_comments%22%3Atrue%7D'
    }
    index += 1


print(result)