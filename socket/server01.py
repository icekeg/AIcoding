from socket import *

IP = '127.0.0.1'

PORT = 50000

BUFLEN = 512

linsenSocket = socket(AF_INET,SOCK_STREAM)

linsenSocket.bind((IP,PORT))

linsenSocket.listen(5)
print(f'start successful,waiting on {PORT}')

dataSocket, addr = linsenSocket.accept()
print('establish a connection:', addr)

while True:
    recevd = dataSocket.recv(BUFLEN)

    if not recevd:
        break

    info = recevd.decode()
    print(f'get infomation: {info}')
    dataSocket.send(f'sever get infomation {info}'.encode())

dataSocket.close()
linsenSocket.close()