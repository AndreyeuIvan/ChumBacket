<<<<<<< HEAD
'''Today I want to practice socket pip'''
import socket

c = socket.socket()

c.connect(('localhost',9999))
while Tru
=======
import socket

c = socket.socket()
c.bind(('localhost', 9999))

c.listen(3)
c,add = c.accept()
while True:
    print(c.renv(1024).decode())
    user = input('C>>>')
    c.send(bytes(user,'utf-8'))
>>>>>>> d871ae935d10c771dc939e2cc966eac22cd5b075
