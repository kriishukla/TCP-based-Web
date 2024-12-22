from socket import *
import sys

# Get command line arguments
server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

# Create a client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server
clientSocket.connect((server_host, server_port))

# Send the HTTP GET request
request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
clientSocket.send(request.encode())

# Receive and print the response from the server
response = clientSocket.recv(4096).decode()
print(response)

# Close the client socket
clientSocket.close()
