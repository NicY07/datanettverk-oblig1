#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a server socket
#Write your code here
serverPort = 6789 # port that is used on server
serverSocket.bind(('', serverPort)) # binding to the server
serverSocket.listen(1)
#End of your code
while True:
	#Establish the connection print('Ready to serve...') connectionSocket, addr = 
	try:
		#Write your code here
		print("Ready to serve...")
		connectionSocket, addr = serverSocket.accept() # accepts a connection
		#End of your code
		message = connectionSocket.recv(1024)#Write your code here #End of your code 
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()#Write your code here #End of your code 

		#Send one HTTP header line into socket
		#Write your code here
		connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
		#End of your code

		#Send the content of the requested file to the client 
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode()) 
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()


	except IOError:
		#Send response message for file not found
    	#Write your code here
		connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
    	#End of your code
		
		#Close client socket
        #Write your code here
		connectionSocket.close()
		#End of your code
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data