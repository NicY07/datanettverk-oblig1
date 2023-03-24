from socket import * #import socket module
import sys #In order to get command line arguments

# The number of command line arguments should be 4
if len(sys.argv) != 4:
    # Explains to the user how to run the HTTP client program
    print("Usage: python client.py server_host server_port filename")
    sys.exit(1)

# Command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]

try:
    clientSocket = socket(AF_INET, SOCK_STREAM) # Creating a TCP socket
except:
    print("Error creating socket: ")
    sys.exit(1)

try:
    clientSocket.connect((host, port)) # Connecting to the server
except:
    print("Error connecting to server: ")
    clientSocket.close()
    sys.exit(1)

# Creating a HTTP GET request
httpRequest = f"GET /{filename} HTTP/1.1\r\nHost: {host}\r\n\r\n"

try:
    # Sending the request to the server
    clientSocket.send(httpRequest.encode())
except:
    print("Error sending data: ")
    clientSocket.close()
    sys.exit(1)

try:
    # Receiving the response from the server
    message = clientSocket.recv(4096)
except:
    print("Error receiving data: ")
    clientSocket.close()
    sys.exit(1)
    
print(message.decode()) # Displaying the response
clientSocket.close() # Closing the socket