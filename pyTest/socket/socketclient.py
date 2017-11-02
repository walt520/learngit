from socket import *
from time import ctime

host = ''
port = 52026
bufsize = 1024
addr = (host, port)

ss = socket(AF_INET,SOCK_STREAM)
ss.bind(addr)
ss.listen(5)

while True:
    print('fuck u')
    cs,cc = ss.accept()
    print('connected form:',cc)
    
    while True:
        data = cs.recv(bufsize).decode()
        if not data:
            break
        cs.send(('[%s]%s'%(ctime(),data)).encode())
    cs.close()
ss.close()

    
