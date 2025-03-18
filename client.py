from socket import *
import argparse
import sys

parser = argparse.ArgumentParser(description='args')
parser.add_argument('-i', '--ip', type=str, default='127.0.0.1')    # default values for easy running, can also be set with options
parser.add_argument('-p', '--port', type=int, default='8001')
parser.add_argument('-f', '--filename', type=str, default='')
args = parser.parse_args()

clientSocket = socket(AF_INET, SOCK_STREAM)
ip = args.ip
port = args.port
filepath = '/' + args.filename

request = 'GET ' + filepath + ' HTTP/1.1'

clientSocket.connect((ip, port))

clientSocket.send(request.encode())
print(clientSocket.recv(1024).decode())