from socket import *
import sys

#TODO add argparse

clientSocket = socket(AF_INET, SOCK_STREAM)
port = 42069
ip = '127.0.0.1'

request = 'GET / HTTP/1.1'

clientSocket.connect((ip, port))

clientSocket.send(request.encode())
print(clientSocket.recv(1024).decode())