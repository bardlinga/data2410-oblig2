
from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM) 

port = 8000
server_ip ='127.0.0.1'
	
serverSocket.bind((server_ip, port)) 
serverSocket.listen(1) 	

while True:
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	try: 
		# ----------------------------------------------------------------
		# Read HTTP request
		request = serverSocket.recv(1024).decode()

		# Parse HTTP request
		lines = request.splitlines()
		request_line = lines[0]
		method, path, version = request_line.split() #TODO

		#--------------------------------------------------------------------
		message = #Write your code here #End of your code
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = #Write your code here #End of your code

		#Send one HTTP header line into socket
		#Write your code here

		#End of your code

		#Send the content of the requested file to the client 
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode()) 
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()


	except IOError:
		#Send response message for file not found
    	#Write your code here

    	#End of your code
		
		#Close client socket
        
        #Write your code here
		
		#End of your code
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data