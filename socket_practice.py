import socket

c = socket.socket()
c.bind(('localhost', 9999))

c.listen(3)
c,add = c.accept()
while True:
    print(c.renv(1024).decode())
    user = input('C>>>')
    c.send(bytes(user,'utf-8'))
