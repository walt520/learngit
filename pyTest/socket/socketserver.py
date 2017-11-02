from socket import *

host = ''
port = 52026
bufsize = 1024
addr = (host,port)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(addr)

while(True):
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(bufsize).decode()
    if not data:
        break
    print(data)
    
tcpCliSock.close()
