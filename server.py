from socket import *
import sys

# setup
serverSocket = socket(AF_INET, SOCK_STREAM) 	# make socket
port = 42069									# declare port and ip for readability
ip = '127.0.0.1'
serverSocket.bind((ip, port))					# bind socket
serverSocket.listen(1) 							# listen on port for up to 1 connection

# request handling
while True:
	clientSocket, addr = serverSocket.accept()
	print(f'Client connected on address {addr}')			# server side monitoring

	try: 
		request = clientSocket.recv(1024).decode()			# parsing http request
		requestLines = request.splitlines()
		requestHeader = requestLines[0]
		method, path, version = requestHeader.split()

		print(f'Handling client request: {requestHeader}')	# server side montioring
		
		responseBody = ""

		if method == 'GET':
			if path == '/':
				path = '/index.html'									# redir empty path to index
			
			responseBody = open('.' + path).read()
			responseHeader = 'HTTP/1.1 200 OK' \
			'\r\n' + 'Content-Type: text/html'							# could also expand response header with Content-Length etc
			response = responseHeader + '\r\n\r\n' + responseBody		# construct response from header and body
		else:															# elif method == other valid methods goes here
			response = 'HTTP/1.1 405 Method not allowed'

	except FileNotFoundError:
		response = 'HTTP/1.1 404 Not found'
	except ValueError:
		response = 'HTTP/1.1 400 Bad request error'			# Handles ValueError thrown by too few values in request header
	except:
		response = 'HTTP/1.1 500 Internal server error'		# General except for other errors
	finally:
		clientSocket.send(response.encode())
		clientSocket.close()
		#serverSocket.close()
		#sys.exit()