import socket
import time
ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2006
print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(1024)
while True:
#    Input = input('Hey there: ')
    time.sleep(1)
    ClientMultiSocket.send(str.encode("test"))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
ClientMultiSocket.close()